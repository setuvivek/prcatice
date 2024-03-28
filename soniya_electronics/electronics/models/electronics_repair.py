from odoo import api, models, fields
from datetime import datetime

class ElectronicRepair(models.Model):
    _name = "electronics.repair"
    _description = "Repair"
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    repair_id = fields.Char(string='Repair Code', copy=False, default='New', readonly=True)
    item_id = fields.Many2one('electronics.items', string='Item', related='customer_id.item_id')
    customer_id = fields.Many2one('electronics.customer', string='Customer')
    fault = fields.Char(string='Fault', compute='_compute_fault')

    def _compute_fault(self):
        for records in self:
            if records.customer_id:
                records.fault = records.customer_id.fault
            else:
                records.fault = False

    @api.model
    def create(self, vals):
        if not vals.get('repair_id'):
            vals['repair_id'] = self.env['ir.sequence'].sudo().next_by_code('my_sequence_code')
            recs = super(ElectronicRepair, self).create(vals)
            return recs

    # @api.model
    # def create(self, vals):
    #     if not vals.get('record_id'):
    #         vals['record_id'] = self.env['ir.sequence'].sudo().next_by_code('my_sequence_code')
    #         res = super(Order, self).create(vals)
    #         return res
