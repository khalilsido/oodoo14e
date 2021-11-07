# -*- coding: utf-8 -*-

from odoo import models, fields

class EnhanceHr(models.Model):
    _name = 'hr.contract'
    _inherit = 'hr.contract'

    phone_allow = fields.Float(string="Phone Allowance",  required=False, )
    house_allow = fields.Float(string="House Allowance", required=False, )
    tran_allow = fields.Float(string="Transportation Allowance", required=False,)
    food_allow = fields.Float(string="Food Allowance", required=False, )
    other_allow = fields.Float(string="Other Allowance", required=False,)


class Enhanceemp(models.Model):
    _name = 'hr.employee'
    _inherit = 'hr.employee'

    bank_name = fields.Char(string="Bank Name", required=False, )
    bank_iban = fields.Char(string="Bank IBAN", required=False, )
    med_name = fields.Char(string="Medical Insurance Company", required=False,)
    med_class = fields.Char(string="Medical Insurance Class", required=False,)
    gosi_no = fields.Char(string="Saudi Gosi Number", required=False,)
