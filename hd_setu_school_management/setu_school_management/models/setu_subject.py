# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuSubject(models.Model):
    _name = 'setu.subject'
    _description = 'Setu Subject'

    #Char
    name = fields.Char(string='Name')

    #m2o
    subject_teacher_id = fields.Many2one('setu.teacher', string='Subject Teacher')

    #o2m
    teacher_ids = fields.One2many('setu.teacher', 'subject_id', string='Another Teacher')
    student_ids = fields.Many2many('setu.student','subject_student', 'subject', 'student', string='Student')
