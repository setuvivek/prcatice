# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuClassRoom(models.Model):
    _name = 'setu.standard.division'
    _description = ' Standard Division'

    #Char
    name = fields.Char(string='Name')

    #Integer
    code = fields.Integer(string="Code")

    #O2m
    student_ids = fields.One2many('setu.student', 'division_id', string='Division')
