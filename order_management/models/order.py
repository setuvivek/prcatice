<<<<<<< HEAD
from odoo import models, fields

class Order(models.Model):
    _name = "order"
    _description = "Order"
    # _rec_name = "date"

    owner_name = fields.Char(string="owner name", required=True)
    address = fields.Char(string="address")
    date = fields.Datetime(string="date")
    payment= fields.Selection(selection=[('cash','CASH'),('online','ONLINE')],string='payment', default="cash")
    order_id = fields.Many2one("product", string="order")
    order_ids = fields.Many2many("product", string="other product")
=======
# -*- coding: utf-8 -*-
from odoo import models, fields

class Order(models.Model):
    _name = 'order'
    _description = 'Order'
    # _rec_name = 'quantity'
    # _order = 'price asc'

    customer_name = fields.Char(string='Customer_Name',help='Customer Name',required=True)
    # product_name = fields.Char(string='Product_Name', help='Product Name',required=True)
    quantity = fields.Integer(string='Product_Quantity', required=True, default='1', help='product quantity')
    order_date = fields.Date(string='Order_Date', help='order confirmation date')
    price = fields.Float(string='Product_Price', help='price of product')
    discount = fields.Boolean(string='Is_there_discount',default=False, help='discount is available or not for this order')
    free_delivery = fields.Boolean(string='Free_Delivery', default=True, help='Delivery charges for shipping')
    current_Date_Time = fields.Datetime(string='current_Date_Time', default=fields.Datetime.now, help='current date and time')
    payment = fields.Selection(selection=[('online','Online'),('cod','COD')], string='Payment_Mode', help='Payment Mode either online or Cash On Delivery(COD)')

    product_id = fields.Many2one('product', string='product_id')

    product_ids = fields.Many2many('product', string='Add More Products')







>>>>>>> adaac1a1aae6a787e125f2b12070b0ae7a95b81c
