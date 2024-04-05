from odoo import fields, models

class CustomerData(models.Model):
    _name = "customer.data"
    _description = "CustomerData"
    _rec_name = "first_name"
    _inherit = ['mail.thread','mail.activity.mixin']

    first_name = fields.Char(string="First_name")
    last_name = fields.Char(string="Last_name")
    age = fields.Integer(string='Age')
    email = fields.Char(string="Email")
    phone = fields.Integer(string='Phone')
    city_id = fields.Many2one("city", string="city")
    country_id = fields.Many2one("country", string="Country")
    state_id = fields.Many2one("state", string="State")