from odoo import models, fields

class Country(models.Model):

    _name = "country"
    _description = "Country"

    country_id = fields.Char(string='Country ID', required=True, copy=False)
    name = fields.Char(string = 'Country Name', help="Help")
    city_idss = fields.One2many('city','city_id', string="Country" )
    # city_name = fields.Char(string='City Name')
    # territorial_state_ids = fields.Many2many("state", string="Territories")
    # ocean_state_ids = fields.Many2many("state", "ocean_state_table", "country_id", "ocean_tate_id", string="Ocean States")
    # pa_id = fields.One2many('partner', string="Country")
