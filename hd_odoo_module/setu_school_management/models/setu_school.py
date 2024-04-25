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
    street = fields.Char(string='Street')
    zip = fields.Char(string='Zip')

    #Integer
    code = fields.Integer(string='Code')
    required_age = fields.Integer(string='Minimum Age')

    #m2o
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')
    user_id = fields.Many2one('res.users', string='User')
    teacher_id = fields.Many2one('setu.teacher', string='Principle')

    #o2m
    student_ids = fields.One2many('setu.student', 'school_id', string='Student')
    teacher_ids = fields.One2many('setu.teacher', 'school_id', string='Teacher')
    school_standard_ids= fields.One2many('setu.standard.standard', 'school_id', string='Standards')


    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name'):
                vals['name'] = 'School'
        res = super(SetuSchool, self).create(vals_list)
        return res



    def action_assign_principle(self):
        return








