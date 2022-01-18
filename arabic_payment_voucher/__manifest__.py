# -*- coding: utf-8 -*-
{
    'name': "arabic_payment_voucher",

    'summary': """
        Allows you to Print an updated payment rcpt and vchr""",

    'description': """
        سند قبض و سند صرف حديث
    """,

    'author': "Smart Beats ",
    'website': "http://www.smartbeats-it.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'reports/report.xml',
        'reports/arabic_payment_rcpt.xml',
        'reports/report2.xml',
        'reports/arabic_payment_vchr.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}