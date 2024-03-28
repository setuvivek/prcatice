from odoo import api, models, fields
from datetime import datetime

class ElectronicRepairRequest(models.Model):
    _name = "electronics.repair.request"
    _description = "Repair"
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    # item_id = fields.Many2one('electronics.items', string='Item', related='customer_id.item_id')
    customer_id = fields.Many2one('electronics.customer', string='Customer')
    paid = fields.Boolean(string='Fault')
    fault = fields.Char(string='Problem')

    item_id = fields.Many2one('electronics.items', string='Select Item')

    def _compute_fault(self):
        for records in self:
            if records.customer_id:
                records.fault = records.customer_id.fault
            else:
                records.fault = False

