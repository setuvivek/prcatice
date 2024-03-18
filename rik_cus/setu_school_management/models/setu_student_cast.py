from odoo import models, fields

class SetuStudentCast(models.Model):
    _name = "setu.student.cast"
    _description = "SetuStudentCast"

    name = fields.Char(string="Name")