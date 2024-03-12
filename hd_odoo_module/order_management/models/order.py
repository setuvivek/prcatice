# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Order(models.Model):
    _name = 'order'
    _description = 'Order'
    # _rec_name = 'quantity'
    # _order = 'price asc'

    customer_name = fields.Char(string='Customer_Name', help='Customer Name', required=True)
    address = fields.Char(string='Address')
    # product_name = fields.Char(string='Product_Name', help='Product Name',required=True)
    quantity = fields.Float(string='Product_Quantity', help='product quantity')
    order_date = fields.Date(string='Order_Date', help='order confirmation date')
    price = fields.Float(string='Product_Price', help='price of product')
    discount = fields.Boolean(string='Is_there_discount', default=False,
                              help='discount is available or not for this order')
    free_delivery = fields.Boolean(string='Free_Delivery', default=True, help='Delivery charges for shipping')
    current_Date_Time = fields.Datetime(string='current_Date_Time', default=fields.Datetime.now,
                                        help='current date and time')
    payment = fields.Selection(selection=[('online', 'Online'), ('cod', 'COD')], string='Payment_Mode',
                               help='Payment Mode either online or Cash On Delivery(COD)')

    product_id = fields.Many2one('product', string='product_id')

    product_ids = fields.Many2many('product', string='Add More Products')

    _sql_constraints = [('check_order_quantity', 'check(quantity > 0)', 'product quantity does not zero or less than zero..'),
                        ('address_length', 'CHECK(LENGTH(address) <= 15)', "Please enter short address"),
                        ('check_price', 'CHECK(price > 0)', 'price should not be zero!'),
                        ]
