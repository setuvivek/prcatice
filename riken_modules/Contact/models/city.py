from odoo import fields, models

class City(models.Model):
    _name = "city"
    _description = "City"
    _rec_name = "name"

    name = fields.Char(string="city name", default="Rajkot")
    pincode = fields.Integer(string="pincode", required=True)
    district = fields.Char(string="district name")
    city_id = fields.Many2one("state", string="State")
    city_idd = fields.Many2one("country", string="Country")
    c_id = fields.One2many("customer", "city_id", string="customer")
