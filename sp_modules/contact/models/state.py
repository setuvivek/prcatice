from odoo import fields, models


class State(models.Model):
    _name = 'state'
    _description = 'State'

    name = fields.Char(string='Name', required=True)
    # capital = fields.Char(string='Capital')
    city_ids = fields.One2many('city', 'state_id', string='Cities')
    country_id=fields.Many2one('country',string='Country')
