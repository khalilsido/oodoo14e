# -*- coding: utf-8 -*-
from odoo import http

# class ArabicPaymentVoucher(http.Controller):
#     @http.route('/arabic_payment_voucher/arabic_payment_voucher/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/arabic_payment_voucher/arabic_payment_voucher/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('arabic_payment_voucher.listing', {
#             'root': '/arabic_payment_voucher/arabic_payment_voucher',
#             'objects': http.request.env['arabic_payment_voucher.arabic_payment_voucher'].search([]),
#         })

#     @http.route('/arabic_payment_voucher/arabic_payment_voucher/objects/<model("arabic_payment_voucher.arabic_payment_voucher"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('arabic_payment_voucher.object', {
#             'object': obj
#         })