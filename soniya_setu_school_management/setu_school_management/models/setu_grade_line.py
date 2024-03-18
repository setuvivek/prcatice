from odoo import models, fields

class GradeLine(models.Model):

    _name = "setu.grade.line"
    _description = "Setu_School"

    from_mark = fields.Integer(string='From Mark')
    to_mark = fields.Integer(string='To Mark')
    grade_name = fields.Char(string='Name')
    fail = fields.Integer(string='Fail')
    grade_id = fields.Many2one('setu.grade', string='Grade')

