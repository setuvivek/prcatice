from odoo import models, fields

class SetuStandardStandard(models.Model):
    _name = "setu.standard.standard"
    _description = "SetuStandardStandard"

    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")