from odoo import models, fields

class SetuMotherTongue(models.Model):
    _name = "setu.mother.tongue"
    _description = "SetuMotherTongue"

    name = fields.Char(string="Name")

