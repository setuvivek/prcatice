# -*- coding: utf-8 -*-
from odoo import models,fields,api

class SetuSchool(models.Model):
    _name = 'setu.school'
    _description = 'Setu School'

    #Char
    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')

    #m2o
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')

    #o2m
    student_ids = fields.One2many('setu.student', 'school_id', string='Student')
    teacher_ids = fields.One2many('setu.teacher', 'school_id', string='Teacher')


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name'):
                vals['name'] = 'School'
        res = super(SetuSchool, self).create(vals_list)
        return res