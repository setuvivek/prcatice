from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ProductProduct(models.Model):
    _inherit='product.product'

    add_product = fields.Boolean(string="Would you like to add product?")
    sale_product_id = fields.Many2one('product.product', string="Which product would you like to add?")



