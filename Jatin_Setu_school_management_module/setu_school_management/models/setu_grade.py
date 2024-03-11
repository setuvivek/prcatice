from odoo import fields, models

class Grade(models.Model):
    _name = "setu.grade"
    _description = "setu_grade"

    name = fields.Char(string="Name")
    grade_lines_ids = fields.One2many("setu.grade.line","grade_id",string="Grade Lines")