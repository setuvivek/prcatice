{
    'name' : 'electronics',
    'version' : '16.0',
    'description' : 'electronics repairing management',
    'depends':['contact'],
    'data' : ['security/ir.model.access.csv',
              'views/electronic_customer_views.xml',
              'views/electronic_items_views.xml',
              'views/electronic_vendor_views.xml',
              'views/electronic_repair_views.xml',
              'views/electronic_repair_request_views.xml',
              'data/my_sequence_module.xml',
              ]

}