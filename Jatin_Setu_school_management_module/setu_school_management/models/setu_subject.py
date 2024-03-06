from odoo import fields, models

class Subject(models.Model):
    _name = "setu.subject"
    _description = "setu_subject"

    name = fields.Char(string="Subject Name" , required=True)
    subject_teacher_id = fields.Many2one("setu.teacher",string="Teacher Id")
    student_ids = fields.Many2many("setu.student",string="Student")

