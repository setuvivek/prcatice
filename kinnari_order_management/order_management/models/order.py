from odoo import fields,models

class Order(models.Model):
    _name = "order1"
    _description = "Order_details"
    # _rec_name = "quantity"
    _order = "quantity"

    name = fields.Char(string="Order Name",required=True)
    quantity = fields.Float(string="Quantity for order", copy=False)
    stock = fields.Boolean(string="Stock available or not", default=True)
    dos = fields.Date(string="Order Date")
    product_id = fields.Many2one('product',string="Product")




