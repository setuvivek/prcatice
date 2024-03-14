# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Stock(models.Model):
    _name = 'stock'
    _description = 'Stock'

    #m2o------------------
    product_id = fields.Many2one('product', string='product_id')

    #Char-----------------
    type = fields.Char(string='Type')

    #Float----------------
    incoming = fields.Float(string='Incoming')
    outgoing = fields.Float(string='Outgoing')