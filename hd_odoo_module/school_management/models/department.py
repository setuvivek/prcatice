# -*- coding: utf-8 -*-
from odoo import models, fields


class Department(models.Model):
    _name = 'department'
    _description = 'Department'



    name = fields.Selection(
        selection=[('it', 'BE IT'), ('ec', 'BE EC'), ('ce', 'BE CE'), ('ee', 'BE Electrical'), ('mech', 'BE Mechanical'),
                   ('chem', 'BE Chemical'), ('nano', 'BE Nano Technology')], string='Name',required=True, help='Department Name')

    course_id = fields.Many2one('course', string='Course')

    student_ids = fields.One2many('student','dept_id', string='Student', help="Student's Department")

    teacher_ids = fields.One2many('teacher','dept_id', string='Teacher', help="Teacher's Department")

    hod_id = fields.Many2one('teacher', string='HOD', required=True)

    vision_mission = fields.Text(string='Vision-Mission')

    # placement = fields.Integer(string='Placement')

    _sql_constraints = [('department_name', 'unique(name)', 'department already exists...')]




