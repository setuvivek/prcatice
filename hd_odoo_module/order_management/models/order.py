# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Order(models.Model):
    _name = 'order'
    _description = 'Order'
    # _rec_name = 'quantity'
    # _order = 'price asc'

    #Char------------------
    customer_name = fields.Char(string='Customer_Name', help='Customer Name', required=True)
    address = fields.Char(string='Address')

    #Float-----------------
    quantity = fields.Float(string='Product_Quantity', help='product quantity')

    #Date------------------
    order_date = fields.Date(string='Order_Date', help='order confirmation date')

    #Float-----------------
    price = fields.Float(string='Product_Price', help='price of product')

    #Boolean---------------
    free_delivery = fields.Boolean(string='Free_Delivery', default=True, help='Delivery charges for shipping')

    #Datetime--------------
    current_Date_Time = fields.Datetime(string='current_Date_Time', default=fields.Datetime.now,
                                        help='current date and time')

    #Selection-------------
    payment = fields.Selection(selection=[('online', 'Online'), ('cod', 'COD')], string='Payment_Mode',
                               help='Payment Mode either online or Cash On Delivery(COD)')
    online = fields.Selection(selection=[('debit', 'Debit Card'), ('credit', 'Credit Card'), ('net_banking', 'Net Banking'), ('mobile wallet', 'Mobile Wallet')])
    mobile_wallet = fields.Selection(selection=[('paytm', 'Paytm'), ('phonepe', 'PhonePe'), ('google_pay','Google Pay')])

    #M2o-------------------
    product_id = fields.Many2one('product', string='product_id', domain=[('discount', '=', '10 to 30%')])

    #M2m------------------
    product_ids = fields.Many2many('product', string='Add More Products')


    #SQL Constrains--------

    _sql_constraints = [('check_order_quantity', 'check(quantity > 0)', 'product quantity does not zero or less than zero..'),
                        ('address_length', 'CHECK(LENGTH(address) <= 15)', "Please enter short address"),
                        ('check_price', 'CHECK(price > 0)', 'price should not be zero!'),
                        ]
