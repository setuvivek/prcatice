# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuClassRoom(models.Model):
    _name = 'setu.grade.line'
    _description = 'Grade Line'

    #Char
    grade_name = fields.Char(string='Name')

    #Integer
    from_mark = fields.Integer(string='From Mark')
    to_mark = fields.Integer(string='To Mark')

    #Boolean
    fail = fields.Boolean(string='Fail')

    #m2o
    grade_id = fields.Many2one('setu.grade', string='Grade')


