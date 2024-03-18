from odoo import fields, models

class SetuGradeLine(models.Model):
    _name = "setu.grade.line"
    _description = "SetuGradeLine"

    from_mark = fields.Integer(string="From Mark")
    to_mark = fields.Integer(string="To mark")
    grade_name = fields.Char(string="Name")
    fail = fields.Selection(selection=[("yes","YES"),("no","NO")], string="Fail")
    grade_id = fields.Many2one("setu.grade", string="Grade")