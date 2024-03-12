from odoo import fields, models

class Customer(models.Model):
    _name = "customer"
    _description = "Customer"

    first_name = fields.Char(string="First_name")
    last_name = fields.Char(string="Last_name")
    customer = fields.Boolean(string="Is customer or not?")
    city_id = fields.Many2one("city", string="city")
    ci_id = fields.Many2many("city", string="City")
    country_id = fields.Many2one("country", string="Country")
    state_id = fields.Many2one("state", string="State")

