# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuTeacher(models.Model):
    _name = 'setu.teacher'
    _description = 'Setu Teacher'


    #Char
    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile')

    #m2o
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')
    school_id = fields.Many2one('setu.school', string='School')
    subject_id = fields.Many2one('setu.subject', string='Subject')

    #o2m
    student_ids = fields.One2many('setu.student','class_teacher_id', string='Student')
    class_ids = fields.Many2many('setu.class','class_teacher_id', string='Class')

