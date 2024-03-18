from odoo import models, fields

class StandardStandard(models.Model):

    _name = "setu.standard.standard"
    _description = "Setu_School"

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')