<<<<<<< HEAD
from odoo import models, fields
=======
# -*- coding: utf-8 -*-
from odoo import fields, models
>>>>>>> adaac1a1aae6a787e125f2b12070b0ae7a95b81c

class Student(models.Model):
    _name = 'student'
    _description = 'Student'

<<<<<<< HEAD
    name = fields.Char(string='Name', required=True, help="validation")
    std = fields.Integer(string='Std')
    cls = fields.Selection(selection=[('a','A'),('b','B')],string='Cls')
    gender = fields.Selection(selection=[('male','MALE'),('female','FEMALE')],string='Gender', default="male")
    age = fields.Integer(string='Age')
    birth_date = fields.Date(string="birth_date")
    teacher_id = fields.Many2one("teacher", string="Teacher")
    teacher_ids = fields.Many2many("teacher", "science_teacher", "student", "teacher", string="science_teacher")
    math_teacher_ids = fields.Many2many("teacher", "math_teacher", "student", "teacher", string="math_teacher")
    city_id = fields.Many2one("city", string="City")
=======

    name = fields.Char(string='Name', required=True,copy=False,help='validated field')
    rollno= fields.Integer(string='Roll No', required=True)
    std = fields.Char(string='Std', required=True)
    phone = fields.Char(string='Phone', unaccent=False)
    email = fields.Char(string='Email')
    gender=fields.Selection(selection=[('male','Male'),('female','Female')],string='Gender')
    birthdate = fields.Datetime(string='Birthdate')
    result = fields.Float(string='CGPA')
    city_id = fields.Many2one('city',string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')
    nationality = fields.Selection(selection=[('indian','Indian'),('foreigner','Foreigner')],string='nationality',default='indian')
    classteacher_id = fields.Many2one('teacher',string='Class Teacher')
    mathteacher_ids = fields.Many2many('teacher','math_teacher', string='Math Teachers')




>>>>>>> adaac1a1aae6a787e125f2b12070b0ae7a95b81c
