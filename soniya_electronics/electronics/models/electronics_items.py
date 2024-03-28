from odoo import api, models, fields
from datetime import datetime
from dateutil.relativedelta import relativedelta

class ElectronicsItems(models.Model):
    _name = "electronics.items"
    _description = "Items"
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name')
    price = fields.Float(string='Price')
    warranty = fields.Char(string='Warranty')
    mfg_date = fields.Date(string='Mfg Date')
    exp_date = fields.Date(string='Exp Date', compute='_compute_exp_date')
    customer_id = fields.Many2one('electronics.customer', string='Customer')
    vendor_id = fields.Many2one('electronics.vendor', string='Vendor')

    @api.model
    def create(self, vals):
        if not vals.get('warranty'):
            vals.update({'warranty':'1year'})
        rec = super(ElectronicsItems, self).create(vals)
        return rec







