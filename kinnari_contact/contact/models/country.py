from odoo import fields, models

class Country(models.Model):
    _name = "country"
    _description = "Country"

    name = fields.Char(string="Name",required=True)
    code = fields.Integer(string="Code")
    type = fields.Boolean(string="devlop country")
    # state_id = fields.Many2many('state','state1',string="State")
    # city_id = fields.Many2many('city','city1', string="City")
    customer_ids = fields.One2many('contact.partner', 'country_id', string="Customer")

