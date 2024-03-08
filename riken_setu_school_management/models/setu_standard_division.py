from odoo import models, fields

class SetuStandardDivision(models.Model):
    _name = "setu.standard.division"
    _description = "SetuStandardDivision"

    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")