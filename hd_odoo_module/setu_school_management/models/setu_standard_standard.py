# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuClassRoom(models.Model):
    _name = 'setu.standard.standard'
    _description = ' Standard Standard'

    #Char
    name = fields.Char(string='Name')

    #Integer
    code = fields.Integer(string="Code")

    #M2o
    subject_id = fields.Many2one('setu.subject', string='Subject')
    school_id = fields.Many2one('setu.school', string='School')
