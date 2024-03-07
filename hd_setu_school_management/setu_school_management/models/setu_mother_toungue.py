# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuClassRoom(models.Model):
    _name = 'setu.mother.tongue'
    _description = 'Mother Tongue'

    #Char
    name = fields.Char(string='Name')
    
    #O2m
    student_ids = fields.One2many('setu.student', 'mother_tongue_id', string='Student')

