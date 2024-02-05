# -*- coding: utf-8 -*-
{
    'name': "QS CRM and Partner Customization",

    'summary': "This module adds, among others, a serializing functionalities to partners",

    'description': """
CRM & Partners
====================
This module adds, among others, a serializing functionalities to partners.

Also it adds a menu in crm that points to purchase orders.
    """,

    'author': "Quick Services Solutions",
    'maintainer': 'Quick Services Solutions',
    'website': "https://www.qs-solutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'purchase'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'data/res_partner_sequence.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}

