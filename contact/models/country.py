from odoo import fields,models

class Country(models.Model):
    _name= 'country'
    _description= 'Country'

    name = fields.Char(string='Name', required=True)
    states_ids=fields.One2many('state','country_id',string='States')
    cities_ids=fields.One2many('city','country_city_id',string='Cities', domain="[('capital','=','True')]")
    capitals_ids=fields.Many2many('city','capitals_ids',string='State Capitals')
