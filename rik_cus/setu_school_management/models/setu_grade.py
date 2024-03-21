from odoo import fields, models

class SetuGrade(models.Model):
    _name = "setu.grade"
    _description = "SetuGrade"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    grade_line_ids = fields.One2many("setu.grade.line", "grade_id", string="Grade Lines")
