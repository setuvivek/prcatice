# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Setu Sale Margin Extended',
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
    'depends': ['sale_margin', 'setu_sa_sale_extended','website'],
    'images': ['static/description/banner.gif'],
    'data': [
        'security/ir.model.access.csv',
        'report/sales_commission_report.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_line_views.xml',
        'views/template.xml',
        'wizard/journal_entry_wizard_view.xml',
        'wizard/sale_commission_wizard_view.xml',
    ],
    'application': True,
}
