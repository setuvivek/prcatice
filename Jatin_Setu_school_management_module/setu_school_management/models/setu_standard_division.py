from odoo import fields, models

class Standard_division(models.Model):
    _name = "setu.standard.division"
    _description = "Setu Standard Division"

    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
