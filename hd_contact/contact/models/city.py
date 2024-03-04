# -*- coding: utf-8 -*-
from odoo import models, fields

class City(models.Model):
    _name = 'city'
    _description = 'City'


    name = fields.Char(string='Name', help='City', required=True)
    code = fields.Integer(string='Pin Code', help='City Pincode Number')

    state_id = fields.Many2one('state', string='State', help='Many2one relation')
    country_id = fields.Many2one('country', string='Country', help='Many2one relation')

    contact_partner_ids = fields.One2many('contact.partner','city_id', string='Contact Partner', help='One2many relation')






