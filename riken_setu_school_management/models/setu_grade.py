from odoo import fields, models

class SetuGrade(models.Model):
    _name = "setu.grade"
    _description = "SetuGrade"

    name = fields.Char(string="Name")
    grade_line_ids = fields.One2many("setu.grade.line", "grade_id", string="Grade Lines")
