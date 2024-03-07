# -*- coding: utf-8 -*-
from odoo import models,fields,api

class SetuStudent(models.Model):
    _name = 'setu.student'
    _description = 'Setu Student'


    #Char
    name = fields.Char(string='Name')
    address = fields.Char(string='Address')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')

    #Integer
    roll_no = fields.Integer(string='Roll No')

    #Date
    dob = fields.Date(string='DOB')

    #m2o
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')
    class_id = fields.Many2one('setu.class', string='Class')
    class_teacher_id = fields.Many2one('setu.teacher', string='Class Teacher')
    school_id = fields.Many2one('setu.school', string='School')

    #m2m
    teacher_ids = fields.Many2many('setu.teacher','student_teacher', 'student', 'teacher', string='Teacher')
    subject_ids = fields.Many2many('setu.subject','student_subject', 'student', 'subject', string='Subject')

    def action_done(self):
        self.env['setu.student'].create({"name":"Hemangi"})

    @api.model_create_multi
    def create(self,vals_list):
        # for vals in vals_list:
        #     if not vals.get('name'):
        #         vals['name'] = 'student'
        res = super(SetuStudent, self).create(vals_list)
        return res




