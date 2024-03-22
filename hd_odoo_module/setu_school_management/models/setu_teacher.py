# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuTeacher(models.Model):
    _name = 'setu.teacher'
    _description = 'Setu Teacher'


    #Char
    name = fields.Char(string='Name')
    work_address = fields.Char(string='Work Address')
    home_address = fields.Char(string='Home Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile')
    street = fields.Char(string='Street')
    zip = fields.Char(string='Zip')
    street2 = fields.Char(string='Street')
    zip2 = fields.Char(string='Zip')

    #Boolean
    is_teacher = fields.Boolean(string='Is Teacher')

    #m2o
    school_id = fields.Many2one('setu.school', string='School')
    standard_id = fields.Many2one('setu.class', string='Responsibility of Academic Class')
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')
    city2_id = fields.Many2one('city', string='City')
    state2_id = fields.Many2one('state', string='State')
    country2_id = fields.Many2one('country', string='Country')
    medium_id = fields.Many2one('setu.standard.medium', string='Medium')
    division_id = fields.Many2one('setu.standard.division', string='Division')
    subject_id = fields.Many2one('setu.subject', string='Subject')



    #o2m
    student_ids = fields.One2many('setu.student','class_teacher_id', string='Student')
    subject_ids = fields.One2many('setu.subject', 'subject_teacher_id', string='Subject')

    def copy(self, default=None):
        return super(SetuTeacher, self).copy(default)


