from odoo import models, fields

class ProductData(models.Model):
    _name = "product"
    _description = "Product"


    product_name = fields.Char(string="product name", copy=False)
    total_quantity = fields.Integer(string="total quantity")
    date = fields.Date(string="date")
    amt = fields.Char(string="amount")
    p_id = fields.One2many("order", "order_id", string="Product")
