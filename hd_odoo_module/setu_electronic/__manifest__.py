 #-*- coding: utf-8 -*
{
    'name': 'Setu Repair',
    'version': '16.1',
    'author':'Setu Consulting Service Pvt.Ltd',
    'website': 'https://www.setuconsulting.com',
    'depends':['contact', 'mail'],
    'license': 'OPL-1',
    'summary': """  
      User can submit request for repair pre define electronics items 
       """,
    'data':[
        'security/ir.model.access.csv',
        'views/setu_electronic_item_views.xml',
        'views/setu_repair_item_views.xml',
        'views/setu_all_request_views.xml',
        'views/setu_customer_views.xml',
        'views/setu_company_views.xml',
    ],
}