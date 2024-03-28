from odoo import fields, models

class Subject(models.Model):
    _name = "setu.subject"
    _description = "setu_subject"

    name = fields.Char(string="Subject Name")
    code = fields.Char(string="Code")
    minimum_marks = fields.Char(string="Minimum Marks")
    maximum_marks = fields.Char(string="Maximum Marks")
    weightage = fields.Char(string="Weightage")
    teacher_ids = fields.Many2many("setu.teacher","subject_teacher_table", string="Teachers")
    standard_ids = fields.Many2many("setu.standard.standard","student_standard_table",string="Standards")
    standard_id = fields.Many2one("setu.standard.standard", string="Class")
    student_ids = fields.Many2many("setu.student", string="Students")


