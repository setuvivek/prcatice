# -*- coding: utf-8 -*-
from odoo import fields, models

class Student(models.Model):
    _name = 'student'
    _description = 'Student'


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




