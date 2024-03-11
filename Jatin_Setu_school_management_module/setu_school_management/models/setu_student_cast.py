from odoo import fields, models

class Student_cast(models.Model):
    _name = "setu.student.cast"
    _description = "Setu Student Cast"

    name = fields.Char(string="Name")
