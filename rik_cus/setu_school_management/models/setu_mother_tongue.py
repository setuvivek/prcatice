from odoo import models, fields

class SetuMotherTongue(models.Model):
    _name = "setu.mother.tongue"
    _description = "SetuMotherTongue"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)

