# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuClass(models.Model):
    _name = 'setu.class'
    _description = 'Setu Class'



    #Char
    name = fields.Char(string='Name')

    #m2o
    class_teacher_id = fields.Many2one('setu.teacher', string='Class Teacher')

    #o2m
    student_ids = fields.One2many('setu.student', 'standard_id', string='Student')
    subject_ids = fields.One2many('setu.subject','standard_id' ,string='Subject')
    admission_form_ids = fields.One2many('setu.admission.form', 'class_id', string='Total Admission')

    #m2m
    teacher_ids = fields.Many2many('setu.teacher','class_teacher', 'class', 'teacher', string='Teacher')
    school_ids = fields.Many2many('setu.school','class_school', 'class', 'school' ,string='School')
