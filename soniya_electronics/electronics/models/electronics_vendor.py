from odoo import api, models, fields

class ElectronicVendor(models.Model):
    _name = "electronics.vendor"
    _description = "Vendor"
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    phone = fields.Integer(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Char(string='Address')
    # vendor_ids = fields.One2many('electronics.items', 'vendor_id', string='Items')
    # customer_ids = fields.One2many('electronics.customer', 'vendor_id', string='Customer')
    item_id = fields.Many2one('electronics.items', string='Item')
    item_price = fields.Float(string='Price', compute='_compute_item_price')

    def _compute_item_price(self):
        for records in self:
            if records.item_id:
                self.item_price = records.item_id.price
            else:
                self.item_price = False