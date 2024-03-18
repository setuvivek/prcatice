from odoo import models, fields

class StandardDivision(models.Model):

    _name = "setu.standard.division"
    _description = "Setu_School"

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')