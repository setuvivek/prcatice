# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Student(models.Model):
    _name = 'student'
    _description = 'Student'
    # _rec_name = 'code'
    _order = 'id desc'

    name = fields.Char(string='Name', help='Student Name')
    roll_no = fields.Integer(string='Roll No', copy=False, help='Student Roll No')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    sem = fields.Selection(
        selection=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')],
        string='Semester', default='1')
    is_present = fields.Boolean(string='is_present')
    student_dob = fields.Date(string="Date of Birth", help='Student Birth Date')

    teacher_id = fields.Many2one('teacher', string='Class Teacher', help='Many2one relation')

    teacher_ids = fields.Many2many('teacher', string='DS Teacher', help='Many2many relation')
    dbms_teacher_ids = fields.Many2many('teacher', 'ds_teacher', 'student', 'teacher', string='DBMS Teacher',
                                        help='Many2many relation')
    oop_teacher = fields.Many2many('teacher', 'oop_teacher', 'student', 'teacher', string='OOP Teacher',
                                   help='Many2many relation')

    course_id = fields.Many2one('course', string='Course', help='Many2one relation')
    dept_id = fields.Many2one('department', string='Department', help='Many2one relation')

    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')

    # @api.model
    # def create(self, vals):
    #     if not vals.get('roll_no'):
    #         vals.update({'roll_no': '1'})
    #     res = super(Student, self).create(vals)
    #     return res

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('roll_no'):
                vals['roll_no'] = '2'

        res = super(Student, self).create(vals_list)
        return res
    # def create(self, vals_list):
    #     vals_list = [{}]
    #     return super(Student, self).create(vals_list)



