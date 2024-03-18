from odoo import api, models, fields

class Class(models.Model):

    _name = "setu.class"
    _description = "Setu_Class"

    name = fields.Char(string='Name')
    class_teacher_id = fields.Many2one('setu.teacher', string='Teacher')
    teacher_ids = fields.Many2many('setu.teacher', string='Teacher')
    student_ids = fields.Many2many('setu.student', string='Student')
    school_ids = fields.Many2many('setu.school', string='School')
    subject_ids = fields.Many2many('setu.subject', string='Subject')


