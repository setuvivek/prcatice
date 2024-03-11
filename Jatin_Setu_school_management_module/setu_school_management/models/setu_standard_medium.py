from odoo import fields, models

class Standard_medium(models.Model):
    _name = "setu.standard.medium"
    _description = "Setu Standard Medium"

    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
