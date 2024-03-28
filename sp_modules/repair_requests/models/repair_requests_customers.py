from odoo import fields, models, api

class RepairRequestsCustomers(models.Model):
    _name='repair.requests.customers'
    _description='Customers'

    name=fields.Char(string='Name',Required=True)

    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    dob = fields.Datetime(string='Birthdate')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    address = fields.Text(string='Address')
    state_id = fields.Many2one('state', string='State')
    city_id = fields.Many2one('city', string='City')

    repair_request_ids=fields.One2many('repair.requests.requests','customer_name_id',string='Repair Requests')
