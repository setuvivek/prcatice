{
    'name': 'Website Sale Extended',
    'summary': "Website Sale Extended",
    'description': "",
    'author': 'Setu Consulting Services Pvt. Ltd.',
    'website': 'https://www.setuconsulting.com',
    'sequence': 25,
    'version': '17.0',
    'depends': ['website', 'website_sale', 'product'],
    'data': [
        'views/product_template_views.xml',
        'views/tempalte.xml',
        'views/leadform.xml',
        'views/stock.xml',
        'views/product_varianta_btn.xml',

    ],
    'assets': {
        'web.assets_frontend': [
            "website_sale_extended/static/src/js/product_variant.js",

        ]
    },

    # 'js': [
    #     'static/src/js/product_variant.js',
    # ],
    'license': 'LGPL-3',
}
