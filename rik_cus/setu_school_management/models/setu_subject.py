from odoo import models, fields

class SetuSubject(models.Model):
    _name = "setu.subject"
    _description = "SetuSubject"
    _rec_name = "name"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    code = fields.Integer(string="Code", tracking=True)
    maximum_marks = fields.Integer(string="Maximum Marks", tracking=True)
    minimum_marks = fields.Integer(string="Minimum Marks", tracking=True)
    weightage = fields.Integer(string="Weightage", tracking=True)
    teacher_ids = fields.Many2many("setu.teacher", string="Teachers")
    standard_ids = fields.Many2many("setu.standard.standard", "subject_standard" "subject" "standard", string="Standards")
    standard_id = fields.Many2one("setu.class", string="Class")
    student_ids = fields.Many2many("setu.student", "subject_student" "subject" "student", string="Students")