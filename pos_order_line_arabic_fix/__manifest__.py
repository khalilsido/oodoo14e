# -*- coding: utf-8 -*-
{
    'name': 'POS Arabic Order Line Fix',
    'summary': 'POS order line fix',
    'description': 'Fix the issue of alignment in RTL languages POS order line when combining both arabic and latin characters.',
    'author': 'Mustafa SAADI, IQSYS',
    'website': 'https://imerps.com',
    'category': 'Point of Sale',
    'version': '14.0.0.0',
    'depends': ['base', 'point_of_sale'],
    'qweb': ['static/src/xml/pos_order_line.xml'],
    'data': [],
    'images': ['static/description/images/main_screenshot.png'],
    'license': 'LGPL-3',
    'auto_install': False,
    'installable': True,
}
