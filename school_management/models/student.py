from odoo import models, fields

class Student(models.Model):
    _name = 'student'
    _description = 'Student'

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
