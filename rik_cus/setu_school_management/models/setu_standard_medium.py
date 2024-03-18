from odoo import models,fields

class SetuStandardMedium(models.Model):
    _name = "setu.standard.medium"
    _description = "SetuStandardMedium"

    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")