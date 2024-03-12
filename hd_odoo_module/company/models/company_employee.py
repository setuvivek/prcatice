# -*- coding: utf-8 -*-
from odoo import models,fields

class Employee(models.Model):
    _name = 'company.employee'
    _description = 'company.employee'

    name = fields.Char(string='Name', required=True)
    code = fields.Integer(string='Code', copy=False)
    address = fields.Text(string='Address')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender', default='female')
    dob = fields.Date(string="Birth Date", help='Employee BirthDate')
    join_date = fields.Datetime(string='Joining Date', help='Employee Join Date')
    is_present = fields.Boolean(string='is_present')
    salary = fields.Float(string='Salary')

    manager_id = fields.Many2one('company.manager', string='Manager')
    project_id = fields.Many2one('company.project', string='Project')

    department_id = fields.Many2one('company.department', string='Department')

    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')


