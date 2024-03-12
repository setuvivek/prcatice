# -*- coding: utf-8 -*-
from odoo import models, fields


class Teacher(models.Model):
    _name = 'teacher'
    _description = 'Teacher'
    # _rec_name = 'code'
    _order = 'id desc'

    name = fields.Char(string='Name',copy=False, required=True, help='Teacher Name')
    code = fields.Char(string='Code',copy=False, help='Teacher Code')
    subject = fields.Selection(selection=[('ds','Data Structure'), ('dbms','DBMS'),('oop','OOP'),('aml','Applied Machine Learning'),('data science','Data Science with Python'),
                                          ('ui/ux',' Agile UI/UX'),('wc','Wireless Communication'),('cn','Computer Network'),('cns','Cryptography and Security'),
                                          ], string='Subject Name')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender', default='male')
    phone = fields.Char(string='Phone No')
    datetime = fields.Datetime(string='current Date Time',default=fields.Datetime.now)
    salary = fields.Float(string='Salary')

    student_ids = fields.One2many('student','teacher_id', string='Student')
    course_id = fields.Many2one('course', string='Course')
    dept_id = fields.Many2one('department', string='Department')

    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')




