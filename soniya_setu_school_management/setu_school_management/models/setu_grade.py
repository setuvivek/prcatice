from odoo import models, fields

class Grade(models.Model):

    _name = "setu.grade"
    _description = "Setu_School"

    name = fields.Char(string='Name')
    grade_line_ids = fields.One2many('setu.grade.line', 'grade_id', string='Grade Lines')
