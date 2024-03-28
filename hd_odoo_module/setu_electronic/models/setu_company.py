# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuCompany(models.Model):
    _name = 'setu.company'
    _description = 'Setu Company'

    #Char------------------------
    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    website = fields.Char(string='Website')
    address = fields.Char(string='Address')
    street = fields.Char(string='Street')
    zip = fields.Char(string='Zip')

    #Integer---------------------
    code = fields.Integer(string='Code')

    # O2m------------------------
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')