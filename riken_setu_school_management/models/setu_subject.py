from odoo import models, fields

class SetuSubject(models.Model):
    _name = "setu.subject"
    _description = "SetuSubject"
    _rec_name = "name"

    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
    maximum_marks = fields.Integer(string="Maximum Marks")
    minimum_marks = fields.Integer(string="Minimum Marks")
    weightage = fields.Integer(string="Weightage")
    teacher_ids = fields.Many2many("setu.teacher", string="Teachers")
    standard_ids = fields.Many2many("setu.standard.standard", "subject_standard" "subject" "standard", string="Standards")
    standard_id = fields.Many2one("setu.class", string="Class")
    student_ids = fields.Many2many("setu.student", "subject_student" "subject" "student", string="Students")