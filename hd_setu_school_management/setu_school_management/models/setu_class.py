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
    student_ids = fields.One2many('setu.student', 'class_id', string='Student')

    #m2m
    teacher_ids = fields.Many2many('setu.teacher','class_teacher', 'class', 'teacher', string='Teacher')
    school_ids = fields.Many2many('setu.school','class_school', 'class', 'school' ,string='School')
    subject_ids = fields.Many2many('setu.subject', 'class_subject', 'class', 'subject',string='Subject')