# -*- coding: utf-8 -*-
from odoo import models, fields


class Course(models.Model):
    _name = 'course'
    _description = 'Course'
    # rec_name = 'name'

    name = fields.Selection(selection=[('eng', 'ENGINEERING'), ('arts', 'ARTS'), ('science', 'Science'),
                                         ('commerce', 'Commerce'), ('management', 'Management'), ('eduction', 'Eduction'),
                                         ('medical', 'Medical'), ('paramedical', 'Paramedical'), ('design', 'Design'),
                                         ('hotel management', 'Hotel Management'), ('computer application', 'Computer Applications'),
                                         ('animation', 'Animation'),
                                         ('law', 'Law'), ('agriculture', 'Agriculture'), ('architecture','Architecture'),
                                         ('veterinary', 'Veterinary Sciences'),
                                         ('pharmacy', 'Pharmacy'), ('aviation', 'Aviation'), ('dental', 'Dental'),
                                         ('vocational222', 'Vocational Courses')], string='Courses', help='course name')

    department_ids = fields.One2many('department', 'course_id', string='Department', help='One2many relation')
    teacher_ids = fields.One2many('teacher', 'course_id', string='Teacher', help='One2many relation')
    student_ids = fields.One2many('student', 'course_id', string='Student', help='One2many relation')

    description = fields.Text(string='Description')

