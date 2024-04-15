# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuResUsers(models.Model):
    _inherit = 'res.users'

    school_id = fields.Many2one('setu_school', string='School')