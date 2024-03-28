from odoo import fields, models

class SetuGradeLine(models.Model):
    _name = "setu.grade.line"
    _description = "SetuGradeLine"
    _inherit = ['mail.thread','mail.activity.mixin']

    from_mark = fields.Integer(string="From Mark", tracking=True)
    to_mark = fields.Integer(string="To mark", tracking=True)
    grade_name = fields.Char(string="Name", tracking=True)
    fail = fields.Selection(selection=[("yes","YES"),("no","NO")], string="Fail")
    grade_id = fields.Many2one("setu.grade", string="Grade", tracking=True)