# -*- coding: utf-8 -*-
from odoo import models, fields,api


class Teacher(models.Model):
    _name = 'teacher'
    _description = 'Teacher'
    # _rec_name = 'code'
    _order = 'id desc'

    #Char--------------------
    name = fields.Char(string='Name',copy=False, required=True, help='Teacher Name')
    code = fields.Char(string='Code',copy=False, help='Teacher Code')
    phone = fields.Char(string='Phone No')

    #Integer
    age = fields.Integer(string='Age')

    #Selection---------------
    subject = fields.Selection(selection=[('ds','Data Structure'), ('dbms','DBMS'),('oop','OOP'),('aml','Applied Machine Learning'),('data science','Data Science with Python'),
                                          ('ui/ux',' Agile UI/UX'),('wc','Wireless Communication'),('cn','Computer Network'),('cns','Cryptography and Security'),
                                          ], string='Subject Name')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender', default='male')

    #Datetime----------------
    datetime = fields.Datetime(string='current Date Time',default=fields.Datetime.now)

    #Float-------------------
    salary = fields.Float(string='Salary')

    #O2m---------------------
    student_ids = fields.One2many('student','teacher_id', string='Student')

    #M2o---------------------
    course_id = fields.Many2one('course', string='Course')
    dept_id = fields.Many2one('department', string='Department')

    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')


    #create-------------------

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            record = self.env['department'].search([('course_id', '=', vals.get('course_id'))], limit=1)
            if record:
                vals.update({'dept_id': record.id})

        res = super(Teacher, self).create(vals_list)
        return res
