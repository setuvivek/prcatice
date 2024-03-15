from odoo import fields, models

class Customer(models.Model):
    _name='contact.partner'
    _description = "Contact.partner"

    name = fields.Char(string="Name")
    check = fields.Boolean(string="Customer", default=False)
    type = fields.Boolean(string="Resident in develop country")
    country_id = fields.Many2one('country',string="Country")
    state_id = fields.Many2one('state',string="State")
    smartcity = fields.Boolean(string="Resident in smartcity")
    city_id = fields.Many2one('city',string="City")
    # type = fields.Selection(selection=[('partner','Partner'),('customer','Customer')] ,string="type")







