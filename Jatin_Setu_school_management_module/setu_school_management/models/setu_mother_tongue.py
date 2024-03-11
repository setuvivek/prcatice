from odoo import fields, models

class Mother_toungue(models.Model):
    _name = "setu.mother.tongue"
    _description = "Setu Mother Tongue"

    name = fields.Char(string="Name")
