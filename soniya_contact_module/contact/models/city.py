from odoo import models, fields

class City(models.Model):

    _name = "city"
    _description = "City"

    city_id = fields.Char(string='City ID', reuired=True, copy=False)
    name = fields.Char(string = 'City Name', required = True)
    # district = fields.Char(string = 'District')
    # country = fields.Char(string = 'Country')
    population = fields.Integer(string='Population', required=True)
    pincode = fields.Integer(string='Pincode', required=True)
    city_ids = fields.Many2one('country', string='Country')
    # partner_id = fields.One2many('partner', string="City")

