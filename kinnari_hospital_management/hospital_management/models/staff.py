from odoo import fields, models

class Staff(models.Model):
    _name = "staff"
    _description = "Staff"


    name=fields.Char(string="Staff Name" , required=True)
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender")
    mobile = fields.Char(string="Mobile")
    address = fields.Boolean(string="You want to add Resident Location")
    age = fields.Integer(string="Age")
    type = fields.Selection(selection=[('nurse','nurse'),('worker','worker'),('a','a'),('b','b')] ,string="Staff Position")
    a = fields.Boolean(string="Boolean")
    state = fields.Selection(selection=[
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('cancel', 'Cancelled'),
        ('done', 'Done'),], string='Status', required=True, readonly=True, copy=False,tracking=True, default='draft')
    country_id = fields.Many2one('country', string="Country Name")
    state_id = fields.Many2one('state', string="State Name")
    city_id = fields.Many2one('city', string="City Name")
