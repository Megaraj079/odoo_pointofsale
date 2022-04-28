  # -*- coding: utf-8 -*-
{
    'name' : 'odoo_sales',
    'version' : '1.1',
    'summary': 'Online odoo_Sales',
    'sequence': 10,
    'description': """
Online Point of Sale    """,
    'category': 'Website',
    'website': '',
    'depends' : [],
    'data': [
        'security/ir.model.access.csv',
        'views/history.xml',
        'views/odooinventory.xml',
        'views/customer.xml',
        'views/odoo_product_details.xml'
      ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,

    'license': 'LGPL-3',
}