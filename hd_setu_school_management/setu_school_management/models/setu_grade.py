# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuClassRoom(models.Model):
    _name = 'setu.grade'
    _description = 'Grade'

    #Char
    name = fields.Char(string='Name')

    #O2m
    grade_line_ids = fields.One2many('setu.grade.line', 'grade_id', string='Grade Lines')


