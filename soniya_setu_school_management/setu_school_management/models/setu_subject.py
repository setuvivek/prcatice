from odoo import models, fields

class Subject(models.Model):

    _name = "setu.subject"
    _description = "Setu_Subject"

    name = fields.Char(string='Name')
    code = fields.Integer(strig='Code')
    maximum_marks = fields.Integer(string='Maximum Marks')
    minimum_marks = fields.Integer(strig='Minimum Marks')
    weightage = fields.Char(string='Weightage')
    # subject_teacher_id = fields.Many2one('setu.teacher', string='Teacher')
    teacher_ids = fields.Many2many('setu.teacher', string='Teacher')
    standard_ids = fields.Many2many('setu.standard.standard', strig='Standard')
    standard_id = fields.Many2one('setu.class',string='Class')
    student_ids = fields.Many2many('setu.student', string='Student')
    # subject_ids = fields.Many2many('setu.subject', string='Subject')


