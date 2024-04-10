# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Product(models.Model):
    _inherit = 'product.product'

    add_more_product = fields.Boolean(string="Add More Products")
    more_product_ids = fields.Many2many('product.product', 'products_products', 'product', 'product_product', string='More Products')

