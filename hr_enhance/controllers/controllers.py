# -*- coding: utf-8 -*-
# from odoo import http


# class HrEnhance(http.Controller):
#     @http.route('/hr_enhance/hr_enhance/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_enhance/hr_enhance/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_enhance.listing', {
#             'root': '/hr_enhance/hr_enhance',
#             'objects': http.request.env['hr_enhance.hr_enhance'].search([]),
#         })

#     @http.route('/hr_enhance/hr_enhance/objects/<model("hr_enhance.hr_enhance"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_enhance.object', {
#             'object': obj
#         })
