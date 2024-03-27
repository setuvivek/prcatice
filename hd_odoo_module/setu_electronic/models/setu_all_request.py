# -*- coding: utf-8 -*-
from odoo import models,fields
from odoo.exceptions import ValidationError

class SetuAllRequest(models.Model):
    _name = 'setu.all.request'
    _description = 'Setu All Request'
    _rec_name = 'repair_item_id'
    _inherit = 'mail.thread', 'mail.activity.mixin'

    #Related-----------------
    repair_description = fields.Char(related='repair_item_id.description', string='Repair Description')

    #M2o---------------------
    repair_item_id = fields.Many2one('setu.repair.item', string='Repair Item')

    def copy(self):
        raise ValidationError('Can not copy this record')
