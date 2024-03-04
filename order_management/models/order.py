from odoo import models, fields

class Order(models.Model):
    _name = "order"
    _description = "Order"
    # _rec_name = "date"

    owner_name = fields.Char(string="owner name", required=True)
    address = fields.Char(string="address")
    date = fields.Datetime(string="date")
    payment= fields.Selection(selection=[('cash','CASH'),('online','ONLINE')],string='payment', default="cash")
    order_id = fields.Many2one("product", string="order")
    order_ids = fields.Many2many("product", string="other product")