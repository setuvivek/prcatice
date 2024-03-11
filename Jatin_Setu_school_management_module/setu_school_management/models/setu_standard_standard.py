from odoo import fields, models

class Standard_standard(models.Model):
    _name = "setu.standard.standard"
    _description = "Setu Standard Standard"

    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
