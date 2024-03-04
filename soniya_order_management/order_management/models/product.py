from odoo import fields, models


class Product(models.Model):
    _name = "product"
    _description = "product model"

    product_id = fields.Integer(string='Product_ID', required=True)
    name = fields.Char(string='Product Name', required=True)
    price = fields.Integer(string='Price', required=True)

    # rel_id = fields.One2many("order", "rel_id", string="Name")
    # rel_ids = fields.Many2many('order', string="Product_Name")
    # rel_ids = fields.Many2many("order", string="Product_Name")