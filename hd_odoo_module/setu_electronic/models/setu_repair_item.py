# -*- coding: utf-8 -*-
from odoo import models, fields,api

class SetuRepairItem(models.Model):
    _name = 'setu.repair.item'
    _description = 'Setu Repair Item'
    _inherit = 'mail.thread', 'mail.activity.mixin'
    _rec_name = 'setu_item_id'

    # Char-----------------------------
    description = fields.Char(string='Repair Description')

    # Float----------------------------
    quantity = fields.Float(string='Product Quantity')

    # Boolean--------------------------
    show_request = fields.Boolean(string='Show Request')

    # related--------------------------
    warranty_expiration = fields.Datetime(related='setu_item_id.warranty', string='Warranty Expiration')
    customer_email = fields.Char(related='customer_id.email', string='Customer Email')
    customer_phone = fields.Char(related='customer_id.phone', string='Customer Phone')

    # M2o------------------------------
    setu_item_id = fields.Many2one('setu.electronic.item', string='Repair Product')
    customer_id = fields.Many2one('setu.customer', string='Customer')

    # O2m------------------------------
    all_request_ids = fields.One2many('setu.all.request', 'repair_item_id', string='All Request')

    def submit_request(self):
        self.all_request_ids.unlink()
        all_request = self.env['setu.all.request']
        for request in self:
            all_request.create({'repair_item_id': request.id})

    # create----------------------------
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            record = self.env['setu.customer'].search([('item_id', '=', vals.get('setu_item_id'))], limit=1)
            if record:
                vals.update({'setu_item_id':record.id})

        res = super(SetuRepairItem, self).create(vals_list)
        return res
