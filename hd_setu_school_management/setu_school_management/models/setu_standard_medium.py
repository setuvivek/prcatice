# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuClassRoom(models.Model):
    _name = 'setu.standard.medium'
    _description = ' Standard Medium'

    #Char
    name = fields.Char(string='Name')

    #Integer
    code = fields.Integer(string="Code")
    
    #O2m
    student_ids = fields.One2many('setu.student', 'medium_id', string='Student')
