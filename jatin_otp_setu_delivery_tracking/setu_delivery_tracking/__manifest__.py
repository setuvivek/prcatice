# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Setu Delivery Tracking',
    'version': '17.0',
    'category': 'sale',
    'summary': """ """,
    'website': 'https://www.setuconsulting.com',
    'support': 'support@setuconsulting.com',
    'description': """
     
    """,
    'author': 'Setu Consulting Services Pvt. Ltd.',
    'license': 'OPL-1',
    'sequence': 25,
    'depends': ['stock','whatsapp_account','whatsapp'],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_view.xml',
        'wizard/otp_verification_wizard.xml',
    ],
    'application': True,
}
