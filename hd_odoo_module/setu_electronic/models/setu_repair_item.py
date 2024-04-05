# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SetuRepairItem(models.Model):
    _name = 'setu.repair.item'
    _description = 'Setu Repair Item'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _rec_name = 'setu_item_id'

    # Char-----------------------------
    description = fields.Char(string='Repair Description')

    # Text------------------------------
    repair_notes = fields.Text(string='Repair Notes')

    # Float----------------------------
    quantity = fields.Float(string='Product Quantity')

    # Boolean--------------------------
    show_request = fields.Boolean(string='Show Request')

    # Selection------------------------
    status = fields.Selection(selection=[('in progress', 'In Progress'), ('complete', 'Complete')])

    # related--------------------------
    warranty_expiration = fields.Datetime(related='setu_item_id.warranty', string='Warranty Expiration')
    customer_email = fields.Char(related='customer_id.email', string='Customer Email')
    customer_phone = fields.Char(related='customer_id.phone', string='Customer Phone')

    # M2o------------------------------
    setu_item_id = fields.Many2one('setu.electronic.item', string='Repair Product')
    customer_id = fields.Many2one('setu.customer', string='Customer', required=True)
    item_company = fields.Many2one(related='setu_item_id.company_id', string='Company')

    # O2m------------------------------
    all_request_ids = fields.One2many('setu.all.request', 'repair_item_id', string='All Request')

    total_request = fields.Integer(string='Current record Request', compute='_compute_request', store=True)


    @api.depends('all_request_ids')
    def _compute_request(self):
        for request in self:
            request.total_request = len(request.all_request_ids)
            # request.total_request = self.env['setu.all.request'].search_count([('repair_item_id', '!=', request.setu_item_id.id)])

    def submit_request(self):
        # self.all_request_ids.unlink()
        all_request = self.env['setu.all.request']
        for request in self:
            all_request.create({'repair_item_id': request.id})

        if 'setu_item_id' in self:
            existing_request = self.env['setu.repair.item'].search(
                [('id', '!=', self.id), ('status', '=', 'in progress'),
                 ('customer_id', '=', 'customer_id')])
            if existing_request.status != 'complete':
                raise ValidationError('The product is currently in repair. Cannot create another repair request....')


    # @api.model
    # def create(self, vals):
    #     if 'setu_item_id' in vals:
    #         existing_request = self.env['setu.repair.item'].search(
    #             [('setu_item_id', '=', vals['setu_item_id']), ('status', '=', 'in progress'),
    #              ('customer_id', '=', vals['customer_id'])])
    #         if existing_request and existing_request.status != 'complete':
    #             raise ValidationError('The product is currently in repair. Cannot create another repair request....')
    #
    #     return super(SetuRepairItem, self).create(vals)





