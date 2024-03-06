from odoo import models, fields

class School(models.Model):

    _name = "setu.school"
    _description = "Setu_School"

    name = fields.Char(string='Name')
    address = fields.Selection(selection=[('rajkot', 'Rajkot'), ('ahemdabad', 'Ahemdabad'), ('jamnagar', 'Jamnagar')], string='Address')
    phone = fields.Integer(string='Phone')
    email = fields.Char(string='email')

