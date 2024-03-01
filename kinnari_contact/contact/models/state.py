from odoo import fields, models

class State(models.Model):
    _name = "state"
    _description = "State"

    name = fields.Char(string="Name",required=True)
    country_id = fields.Many2one('country',string="Country")
    city_ids = fields.One2many('city', 'state_id' , string="City")
    customer_ids = fields.One2many('contact.partner', 'state_id', string="Customer")

