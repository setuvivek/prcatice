from odoo import models, fields


class Order(models.Model):
    _name = "order"
    _description = "order management"

    # order_id = fields.Char(string='order_ID', required=True)
    name = fields.Char(string='Product Name', required=True)
    price = fields.Integer(string='Price', required=True)
    orde_id = fields.Many2one("product", string="Name")
    order_ids = fields.Many2many("product", string="Orders")
    product_ids = fields.Many2one("country", string="Country")

