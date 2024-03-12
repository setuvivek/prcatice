# -*- coding: utf-8 -*-
from odoo import models,fields

class Customer(models.Model):
    _name = 'company.customer'
    _description = 'company.customer'

    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender', default='female')
    dob = fields.Date(string="Birth Date", help='Customer BirthDate')

    project_id = fields.Many2one('company.project', string='Project')