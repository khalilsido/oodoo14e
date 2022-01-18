# -*- coding: utf-8 -*-

from odoo import models, fields, api

class accpayment(models.Model):
    _name = 'account.payment'
    _inherit = 'account.payment'

    m_rcpt = fields.Char(string="Manual Receipt Voucher No", required=False, )
