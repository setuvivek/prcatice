from odoo import fields,models

class SetuStandardStandard(models.Model):
    _name = 'setu.standard.standard'
    _description = 'Standard Standard'

    name = fields.Char(string='Name', required=True)
    code=fields.Char(string='Code')