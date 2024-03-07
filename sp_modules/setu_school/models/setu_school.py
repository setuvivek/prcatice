from odoo import fields, models


class SetuSchool(models.Model):
    _name = 'setu.school'
    _description = 'School model'

    name = fields.Char(string='Name', require=True)
    code=fields.Char(string='Code')
    street = fields.Text(string='Street')
    city_id = fields.Many2one('city',string='City')
    state_id = fields.Many2one('state',string='State')
    zip=fields.Integer(string='Zip')
    country_id = fields.Many2one('country', string='Country')
    phone = fields.Char(string='Phone', unaccent=False)
    email = fields.Char(string='Email')
    required_age=fields.Integer(string='Reuired Age')
    school_standard_ids=fields.Many2many('setu.standard.standard','school_standard_ids',string='School Standards')

