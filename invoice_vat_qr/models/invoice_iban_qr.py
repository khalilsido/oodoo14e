# -*- coding: utf-8 -*-
# Copyright 2019 Openworx
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

import qrcode
import base64
from io import BytesIO
from odoo import models, fields, api
from odoo.http import request
from odoo import exceptions, _


class QRCodeInvoice(models.Model):
    _inherit = 'account.move'

    sa_confirmation_datetime = fields.Datetime(string='Confirmation Date', copy=False)
    qr_image = fields.Binary("QR Code", compute='_compute_sa_qr_code_str')
    total_discount = fields.Monetary(compute="get_total_discount_lines")

    @api.depends('amount_total', 'amount_untaxed', 'sa_confirmation_datetime', 'company_id', 'company_id.vat')
    def _compute_sa_qr_code_str(self):
        """ Generate the qr code for Saudi e-invoicing. Specs are available at the following link at page 23
        https://zatca.gov.sa/ar/E-Invoicing/SystemsDevelopers/Documents/20210528_ZATCA_Electronic_Invoice_Security_Features_Implementation_Standards_vShared.pdf
        """

        def get_qr_encoding(tag, field):
            company_name_byte_array = field.encode('UTF-8')
            company_name_tag_encoding = tag.to_bytes(length=1, byteorder='big')
            company_name_length_encoding = len(company_name_byte_array).to_bytes(length=1, byteorder='big')
            return company_name_tag_encoding + company_name_length_encoding + company_name_byte_array

        for record in self:
            qr_code_str = ''
            if record.sa_confirmation_datetime and record.company_id.vat:
                seller_name_enc = get_qr_encoding(1, record.company_id.display_name)
                company_vat_enc = get_qr_encoding(2, record.company_id.vat)
                time_sa = fields.Datetime.context_timestamp(self.with_context(tz='Asia/Riyadh'),
                                                            record.sa_confirmation_datetime)
                timestamp_enc = get_qr_encoding(3, time_sa.isoformat())
                invoice_total_enc = get_qr_encoding(4, str(record.amount_total))
                total_vat_enc = get_qr_encoding(5, str(record.currency_id.round(
                    record.amount_total - record.amount_untaxed)))

                str_to_encode = seller_name_enc + company_vat_enc + timestamp_enc + invoice_total_enc + total_vat_enc
                qr_code_str = base64.b64encode(str_to_encode).decode('UTF-8')
            record.qr_image = generate_qr_code(qr_code_str)

    def _post(self, soft=True):
        res = super()._post(soft)
        for record in self:
            if record.move_type in ('out_invoice', 'out_refund'):
                self.write({
                    'sa_confirmation_datetime': fields.Datetime.now()
                })
        return res

    def get_total_discount_lines(self):
        for rec in self:
            total = 0.0
            rec.total_discount = 0.0
            for line in rec.invoice_line_ids:
                if line.discount:
                    total += line.price_unit * line.discount / 100
                    rec.total_discount = total

    #    @api.one
    # def _generate_qr_code(self):
    #     service = 'BCD'
    #     # Check if BIC exists: version 001 = BIC, 002 = no BIC
    #     if self.company_id.iban_qr_number.bank_id.bic:
    #         version = '001'
    #     else:
    #         version = '002'
    #     code = '1'
    #     function = 'SCT'
    #     amount_untaxed = str(self.amount_untaxed)
    #     amount_untaxed = ''.join(['Amount untaxed :  ', str(self.amount_untaxed), ' ', self.currency_id.name])
    #     amount_tax = str(self.amount_tax)
    #     amount_tax = ''.join(['Amount tax :  ', str(self.amount_tax), ' ', self.currency_id.name])
    #     amount_total = str(self.amount_total)
    #     amount_total = ''.join(['Amount Total :   ', str(self.amount_total), ' ', self.currency_id.name])
    #
    #     bic = self.company_id.iban_qr_number and self.company_id.iban_qr_number.bank_id.bic or ''
    #     company = ''.join(['Company Name :  ', self.company_id.name])
    #     vat = ''.join(['Company Vat ID :  ', self.company_id.vat])
    #     iban = self.company_id.iban_qr_number and self.company_id.iban_qr_number.acc_number.replace(' ', '') or ''
    #     currency = ''.join([self.currency_id.name, str(self.amount_residual)])
    #     reference = ''.join(['Invoice Number :  ', str(self.name)])
    #     date_time = ''.join(['Date\Time :  ', str(self.create_date)])
    #     lf = '\n'
    #     ibanqr = lf.join([company, vat, date_time, reference, amount_untaxed, amount_tax, amount_total, ])
    #     print(ibanqr)
    #     if len(ibanqr) > 331:
    #         raise exceptions.except_orm(_('Error'),
    #                                     _('IBAN QR code "%s" length %s exceeds 331 bytes') % (ibanqr, len(ibanqr)))
    #     self.qr_image = generate_qr_code(ibanqr)


def generate_qr_code(value):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=20,
        border=4,
    )
    qr.add_data(value)
    qr.make(fit=True)
    img = qr.make_image()
    temp = BytesIO()
    img.save(temp, format="PNG")
    qr_img = base64.b64encode(temp.getvalue())
    return qr_img


class AccountMoveLineInherit(models.Model):
    _inherit = 'account.move.line'

    tax_amount = fields.Float(string="Tax Amount", compute="_compute_tax_amount")

    @api.depends('tax_ids', 'price_unit', 'quantity')
    def _compute_tax_amount(self):
        for line in self:
            if line.tax_ids:
                line.tax_amount = line.price_total - line.price_subtotal
            else:
                line.tax_amount = 0.0
