# -*- coding: utf-8 -*-
from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    school_id = fields.Many2one('setu.school', string='School')
    subject_id = fields.Many2one('setu.subject', string='Subject')