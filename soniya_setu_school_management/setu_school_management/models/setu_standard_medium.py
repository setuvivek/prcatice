from odoo import models, fields

class StandardMedium(models.Model):

    _name = "setu.standard.medium"
    _description = "Setu_School"

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')