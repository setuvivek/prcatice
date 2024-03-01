from odoo import fields, models

class Order(models.Model):
    _name = "order"
    _description = "order"
    # _rec_name = "no_of_order"
    # _order = 'date desc'
    name = fields.Char(string='Order Name' ,required = True)
    no_of_order = fields.Integer(string='No Of Order')
    address = fields.Char(string='Address')
    date = fields.Date(string="Todays Date")
    DateTime = fields.Datetime(string="Datetime")
    product_ids = fields.One2many("product","order_id",string="Product IDS")
    pro_many_ids = fields.Many2many("product",string="Order Name")