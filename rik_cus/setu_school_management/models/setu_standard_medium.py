from odoo import models,fields

class SetuStandardMedium(models.Model):
    _name = "setu.standard.medium"
    _description = "SetuStandardMedium"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    code = fields.Integer(string="Code", tracking=True)