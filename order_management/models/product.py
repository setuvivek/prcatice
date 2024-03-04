<<<<<<< HEAD
from odoo import fields, models

class Product(models.Model):
    _name = 'product'
    _description = 'product data'
    #_inherit = "hr.employee"

    name = fields.Char(string='Name', required=True)
    category = fields.Selection([('electronic','electronic'),('non-electronic','non-electronic')], string='Category')
    price = fields.Integer(string='Price')
    # price = fields.Monetary(string='Price')
    rating = fields.Float(string='Rating')
    mfgdate = fields.Date(string='Mfg Date')
    status = fields.Boolean(string='Status')
=======
# -*- coding: utf-8 -*-
from odoo import models, fields


class Product(models.Model):
    _name = 'product'
    _description = 'Product'
    # _rec_name = 'category'
    # _order = 'price asc'

    name = fields.Char(string='Name',required=True, copy=False, help='Product Name')

    category = fields.Selection(
        selection=[('clothing', 'Clothing'), ('personal care products', 'Personal Care Products'),
                   ('household', 'Household'), ('books', 'Books'), ('phone', 'Phones'), ('toys', 'Toys'),
                   ('electronics', 'Electronics'), ('smart watches', 'Smart Watches'), ('grocery', 'Grocery'),
                   ('beauty & more', 'Beauty & More'), ('wedding store', 'Wedding Store'), ('sports', 'Sports'),
                   ('fitness', 'Fitness'), ('home decore', 'Home Decore'), ('kitchen store', 'Kitchen Store')],
        string='Category', help='product category')

    description = fields.Text(string='Product_description', help='About Product')

    discount = fields.Selection(
        selection=[('no discount', 'No Discount'), ('10 to 30%', '10 To 30%'), ('30 to 50%', '30 To 50%'),
                   ('above 50%', 'Above 50%')], string='Discount', default='no discount', help='About product discount')

    price = fields.Float(string='Price', help='Product Price')

    available = fields.Boolean(string='product_is_available', help='product is available or not')

    order_ids = fields.One2many('order', 'product_id', string='Order')




>>>>>>> 25fd018ac57293e82e63327c861418ace2f89b56
