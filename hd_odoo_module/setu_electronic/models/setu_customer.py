# -*- coding: utf-8 -*-
from odoo import models,fields

class SetuCustomer(models.Model):
    _name = 'setu.customer'
    _description = 'Setu Customer'
    _inherit = 'mail.thread', 'mail.activity.mixin'

    #Char----------------------
    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    street = fields.Char(string='Street')
    zip = fields.Char(string='Zip')

    #O2m-----------------------
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')

    item_id = fields.Many2one('setu.electronic.item', string='Repair Product')
