# -*- coding: utf-8 -*-
from odoo import models,fields
from odoo.exceptions import ValidationError

class SetuAllRequest(models.Model):
    _name = 'setu.all.request'
    _description = 'Setu All Request'
    _rec_name = 'repair_item_id'
    _inherit = 'mail.thread', 'mail.activity.mixin'

    #Char--------------------
    repair_description = fields.Char(string='Repair Description')

    #M2o---------------------
    repair_item_id = fields.Many2one('setu.repair.item', string='Repair Item')

    #Selection---------------
    status = fields.Selection(selection=[('in progress','In Progress'), ('complete','Complete')])

    #Related----------------
    item_customer = fields.Many2one(related='repair_item_id.customer_id', string='Customer')

    def copy(self):
        raise ValidationError('Can not copy this record')