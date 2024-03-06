# -*- coding: utf-8 -*-
from odoo import models, fields


class ContactPartner(models.Model):
    _name = 'contact.partner'
    _description = 'contact.partner'

    name = fields.Char(string='Name', required=True)
    customer = fields.Boolean(string="Is It Customer", help='Partner is Customer or not')

    city_id = fields.Many2one('city', string='City', help='Many2one relation')
    state_id = fields.Many2one('state', string='State', help='Many2one relation')
    country_id = fields.Many2one('country', string='Country', help='Many2one relation')


