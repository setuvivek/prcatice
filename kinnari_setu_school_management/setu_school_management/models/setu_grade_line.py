from odoo import fields, models

class Grade_line(models.Model):
    _name = "setu.grade.line"
    _description = "setu_grade_line"

    from_mask = fields.Char(string="From Mask")
    to_mask = fields.Char(string="To Mask")
    grade_name = fields.Char(string="Name")
    fail = fields.Char(string="Fail")
    grade_id = fields.Many2one("setu.grade",string="Grade")
