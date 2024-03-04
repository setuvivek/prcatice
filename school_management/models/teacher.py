<<<<<<< HEAD
from odoo import models, fields

class Teacher(models.Model):

    _name = "teacher"
    _description = "Teacher"
    _rec_name = "name"
    _order = "age desc"

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection(selection=[('male', 'MALE'), ('female', 'FEMALE')], string='Gender',default="male")
    age = fields.Integer(string='Age')
    phn_no = fields.Integer(string='Phn_No')
    city = fields.Char(string='City')
    joining_date = fields.Datetime(string="joining_date")
    student_ids = fields.One2many("student", "teacher_id", string="Student")
    department_ids = fields.One2many("department", "teacher_id", string="department")

    #department_id = fields.Many2one("department", string="department")
=======
# -*- coding: utf-8 -*-
from odoo import fields, models


class Teacher(models.Model):
    _name = 'teacher'
    _description = 'Teacher'
    # _rec_name = 'code'

    name = fields.Char(string='Name', required=True)
    code = fields.Char(string='code', required=True)
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    phone = fields.Char(string='Phone', unaccent=False)
    email = fields.Char(string='Email')
    subject = fields.Char(string='Subject', required=True)
    city_id = fields.Many2one('city',string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')
    department_id = fields.Many2one('department', string='Department')
    hod=fields.Boolean(string='Hod')
    student_ids = fields.One2many('student', 'classteacher_id', string='Class Students')

>>>>>>> adaac1a1aae6a787e125f2b12070b0ae7a95b81c
