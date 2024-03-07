# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuClassRoom(models.Model):
    _name = 'setu.class.room'
    _description = 'Class Room'

    #Char
    name = fields.Char(string='Name')

    #Integer
    number = fields.Integer(string="Room Number")
