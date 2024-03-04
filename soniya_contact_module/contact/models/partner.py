from odoo import models, fields

class Partner(models.Model):

    _name = "partner"
    _description = "Partner"



    name = fields.Char(string='Name', required = True)
    check = fields.Boolean(string='Partner is customer or not')
    partner_id = fields.Many2many('city', string="City")
    country_ids = fields.Many2many('country', string="Country")
    state_ids = fields.Many2many('state', string="State")
    country_id = fields.Many2one('country', string="Nationality")

