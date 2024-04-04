from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    extra_price=fields.Integer(string='Extra Price')





