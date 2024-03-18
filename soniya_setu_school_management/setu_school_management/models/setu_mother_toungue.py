from odoo import models, fields

class MotherToungue(models.Model):

    _name = "setu.mother.toungue"
    _description = "Setu_School"

    name = fields.Char(string='Name')
