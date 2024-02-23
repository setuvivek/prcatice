from odoo import fields, models

class City(models.Model):
    _name = "city"
    _description = "city"

    name = fields.Char(string="City Name" , required=True)
    district = fields.Char(string="District")
    state = fields.Char(string="State name")
    country = fields.Char(string="Country Name")
    villages = fields.Integer(string="No. of Villages")
    state_id = fields.Many2one("state",string="State Of City")
    country_id = fields.Many2one("country",string="Country Of City")

