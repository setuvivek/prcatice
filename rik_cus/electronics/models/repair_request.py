from odoo import models, fields, api

class RepairRequest(models.Model):
    _name = 'repair.request'
    _description = 'RepairRequest'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Many2one('customer.data', string='Name')
    age = fields.Integer(string='Age')
    item_id = fields.Many2many('electronic.items', 'electronic_items_repair_request_rel' 'item' 'request',string="Select Item")
    urgent = fields.Boolean(string="Is Urgent")

    # customer_email = fields.Char(compute="_compute_display_email", string="Customer Email")
    # customer_phone = fields.Integer(compute="_compute_display_phone", string="Customer Phone")

    # @api.depends('name')
    # def _compute_display_email(self):
    #     for rec in self:
    #         if rec.first_name:
    #             rec.email = rec.first_name.customer_email
    #         else:
    #             rec.customer_email = False
    #
    # def _compute_display_phone(self):
    #     for rec in self:
    #         if rec.first_name:
    #             rec.customer_phone = rec.first_name.customer_phone
    #         else:
    #             rec.customer_phone = False