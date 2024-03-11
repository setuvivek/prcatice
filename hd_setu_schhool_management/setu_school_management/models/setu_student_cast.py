# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuClassRoom(models.Model):
    _name = 'setu.student.cast'
    _description = 'Student Cast'

    #Char
    name = fields.Char(string='Name')


