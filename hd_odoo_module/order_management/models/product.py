# -*- coding: utf-8 -*-
from odoo import models, fields


class Product(models.Model):
    _name = 'product'
    _description = 'Product'
    # _rec_name = 'category'
    # _order = 'price asc'

    # Char
    name = fields.Char(string='Name', required=True, copy=False, help='Product Name')
    description = fields.Char(string='Product_description', help='About Product')
    type = fields.Char(string='Type')

    # Integer
    code = fields.Integer(string='Code')

    # Float
    incoming = fields.Float(string='Incoming Quantity')
    outgoing = fields.Float(string='Outgoing Quantity')
    price = fields.Float(string='Price', help='Product Price')

    # Selection
    category = fields.Selection(
        selection=[('clothing', 'Clothing'), ('personal care products', 'Personal Care Products'),
                   ('household', 'Household'), ('books', 'Books'), ('phone', 'Phones'), ('toys', 'Toys'),
                   ('electronics', 'Electronics'), ('smart watches', 'Smart Watches'), ('grocery', 'Grocery'),
                   ('beauty & more', 'Beauty & More'), ('wedding store', 'Wedding Store'), ('sports', 'Sports'),
                   ('fitness', 'Fitness'), ('home decore', 'Home Decore'), ('kitchen store', 'Kitchen Store')],
        string='Category', help='product category')

    discount = fields.Selection(
        selection=[('no discount', 'No Discount'), ('10 to 30%', '10 To 30%'), ('30 to 50%', '30 To 50%'),
                   ('above 50%', 'Above 50%')], string='Discount', default='no discount', help='About product discount')

    # Boolean
    available = fields.Boolean(string='product_is_available', help='product is available or not')

    order_ids = fields.One2many('order', 'product_id', string='Order')

    _sql_constraints = [('Product_unique', 'unique(name)', 'product already exits....'),
                        ('name_no_spaces', "CHECK(name NOT LIKE '% %')",
                         "Name cannot contain spaces"),
                        ('code_unique', 'unique(code)',
                         'Different products have different code. \n This code already exists.... \n Please use another code!'),
                        ('check_price', 'CHECK(price > 0)', 'price should not be zero!'),
                        ('check_product_type',
                         "CHECK(type IN ('incoming', 'outgoing') AND type IS NOT NULL)",
                         'Please Enter valid customer type...'),
                        ('check_product_quantity', 'CHECK(incoming >= outgoing)',
                         'Outgoing quantity does not greater than incoming quantity! \n outgoing does not exixts stock....'),
                        ]

