from odoo import fields, models

class Country(models.Model):
    _name = "country"
    _description = "Country"

    name = fields.Char(string="country name")
    direction = fields.Selection(selection=[("east","East"),("west","WEST"),("south","SOUTH"),("north","NORTH")], string="In which side of world?", default="north")
    state_ids = fields.One2many("state", "country_id", string="state")
    city = fields.One2many("city", "city_idd", string="city")
    c_id = fields.One2many("customer", "country_id", string="customer")


