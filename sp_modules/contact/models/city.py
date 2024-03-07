from odoo import fields,models

class City(models.Model):
    _name='city'
    _description='city'

    name=fields.Char(string='Name',required=True)
    state_id=fields.Many2one('state',string='State')
    country_city_id=fields.Many2one('country',string='Country')
    capital=fields.Boolean(string='Capital')