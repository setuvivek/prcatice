from odoo import models, fields

class SetuStandardStandard(models.Model):
    _name = "setu.standard.standard"
    _description = "SetuStandardStandard"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    code = fields.Integer(string="Code", tracking=True)