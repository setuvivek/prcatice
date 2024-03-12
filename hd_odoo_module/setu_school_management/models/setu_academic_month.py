# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuAcademicMonth(models.Model):
    _name = 'setu.academic.month'
    _description = 'Academic Month'

    #Char
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')

    #Date
    date_start = fields.Date(string='Date Start')
    date_stop = fields.Date(string='Date Stop')

    #M2o
    academic_year_id = fields.Many2one('setu.academic.year', string='Year')



