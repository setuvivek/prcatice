from odoo import fields, models

class Product(models.Model):
    _name = 'product'
    _description = 'product data'
    #_inherit = "hr.employee"

    name = fields.Char(string='Name', required=True)
    category = fields.Selection([('electronic','electronic'),('non-electronic','non-electronic')], string='Category')
    price = fields.Integer(string='Price')
    # price = fields.Monetary(string='Price')
    rating = fields.Float(string='Rating')
    mfgdate = fields.Date(string='Mfg Date')
    status = fields.Boolean(string='Status')
