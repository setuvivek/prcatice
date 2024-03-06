from odoo import models, fields

class Subject(models.Model):

    _name = "setu.subject"
    _description = "Setu_Subject"

    name = fields.Char(string='Name')
    subject_teacher_id = fields.Many2one('setu.teacher', string='Teacher')
    student_ids = fields.Many2many('setu.student', string='Student')


