from odoo import models, fields

class StudentCast(models.Model):

    _name = "setu.student.cast"
    _description = "Setu_School"

    name = fields.Char(string='Name')
