from odoo import fields ,models

class SetuClass(models.Model):
    _name ='setu.class'
    _description='Class'

    name=fields.Char(string='Name',require=True)
    class_teacher_id=fields.Many2one('setu.teacher',string='Class teacher ID')
    teacher_ids=fields.Many2many('setu.teacher','class_ids',string='Teacher IDs')
    student_ids=fields.One2many('setu.student','class_id',string='Student IDs')
    school_ids=fields.Many2one('setu.school',string='School IDs')
    subject_ids=fields.Many2many('setu.subject','class_subject_ids',string='Subject IDs')