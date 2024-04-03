# -*- coding: utf-8 -*-
from odoo import models,fields,api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    extra_price = fields.Float(string='Extra Price')

