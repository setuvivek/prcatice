# -*- coding: utf-8 -*-
from odoo import models,fields

class Country(models.Model):
    _name = 'country'
    _description = 'Country'


    name = fields.Char(string='Name', help='Country Name', required=True)


    state_ids = fields.One2many('state','country_id', string='State', help='One2many relation')
    city_ids = fields.One2many('city','country_id', string='City', help='One2many relation')

    territories_state = fields.Many2many('state',string='Territories', help='Many2many relation')
    ocean_state = fields.Many2many('state', 'ocean', 'country', 'ocean_state', string='Ocean', help='Many2many relation')

    contact_partner_ids = fields.One2many('contact.partner', 'country_id', string='Contact Partner', help='One2many relation')


