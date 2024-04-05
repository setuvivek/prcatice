from odoo import models, fields, api


class ElectronicItems(models.Model):
    _name = 'electronic.items'
    _description = 'ElectronicItems'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Item Name")
    cost = fields.Float(string="Cost")
    # repair_request_id = fields.Many2one('repair.request', string='Repair Id')