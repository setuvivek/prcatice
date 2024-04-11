# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductProduct(models.Model):
    _inherit = 'product.product'

    add_more_product = fields.Boolean(string="Add More Products")
    more_product_ids = fields.Many2many('product.product', 'products_products', 'product', 'product_product', string='More Products')
    
    
    
class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(selection_add=[
        ('practice', 'Practice Product')
    ], tracking=True, ondelete={'practice': 'set consu'})


