# -*- coding: utf-8 -*-
from odoo import models,fields

class State(models.Model):
    _name = 'state'
    _description = 'State'

    name = fields.Char(string='Name', help='State Name', required=True)

    country_id = fields.Many2one('country', string='Country', help='Many2one relation')
    city_ids = fields.One2many('city','state_id', string='City', help='Many2one relation')

    contact_partner_ids = fields.One2many('contact.partner', 'state_id', string='Contact Partner', help='One2many relation')



