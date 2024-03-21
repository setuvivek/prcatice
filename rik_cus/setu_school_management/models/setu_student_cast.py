from odoo import models, fields

class SetuStudentCast(models.Model):
    _name = "setu.student.cast"
    _description = "SetuStudentCast"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)