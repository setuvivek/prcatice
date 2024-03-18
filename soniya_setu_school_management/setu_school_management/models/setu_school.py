from odoo import models, fields

class School(models.Model):

    _name = "setu.school"
    _description = "Setu_School"

    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    street = fields.Char(string='Street')
    city = fields.Char(string='City')
    state_id = fields.Many2one('state', string='State')
    zip = fields.Integer(string='Zip')
    country_id = fields.Many2one('country', string='Country')
    required_age = fields.Integer(string='Required Age')
    school_standard_ids = fields.Many2many('setu.standard.standard', string='Standard')
    # address = fields.Selection(selection=[('rajkot', 'Rajkot'), ('ahemdabad', 'Ahemdabad'), ('jamnagar', 'Jamnagar')], string='Address')


    # code
    # street
    # city
    # state_id
    # zip
    # country_id
    # required_age
    # school_standard_ids

