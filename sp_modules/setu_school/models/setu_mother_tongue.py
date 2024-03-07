from odoo import fields,models

class SetuMotherTongue(models.Model):
    _name = 'setu.mother.tongue'
    _description = 'Mother Tongue'

    name = fields.Char(string='Name', required=True)
