# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuSubject(models.Model):
    _name = 'setu.subject'
    _description = 'Setu Subject'

    #Char
    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    weightage = fields.Char(string='Weightage')

    #Integer
    maximum_marks = fields.Integer(string='Maximum Marks')
    minimum_marks = fields.Integer(string='Minimum Marks')

    #m2o
    subject_teacher_id = fields.Many2one('setu.teacher', string='Subject Teacher')
    standard_id = fields.Many2one('setu.class', string='Class')
    user_id = fields.Many2one('res.users', string='Users')

    #o2m

    standard_ids = fields.One2many('setu.standard.standard', 'subject_id', string='Standards')

    #M2m
    student_ids = fields.Many2many('setu.student', 'subject_student', 'subject', 'student', string='Student')
