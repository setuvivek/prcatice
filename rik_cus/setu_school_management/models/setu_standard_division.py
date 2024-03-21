from odoo import models, fields

class SetuStandardDivision(models.Model):
    _name = "setu.standard.division"
    _description = "SetuStandardDivision"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    code = fields.Integer(string="Code", tracking=True)