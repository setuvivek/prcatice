# -*- coding: utf-8 -*-
from odoo import models,fields

class Manager(models.Model):
    _name = 'company.manager'
    _description = 'company.manager'

    name = fields.Char(string='Name', required=True)
    street = fields.Char(string='Street')
    zip = fields.Char(string='Zip')
    code = fields.Integer(string='Code', copy=False)
    address = fields.Text(string='Address')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender', default='female')
    dob = fields.Date(string="Birth Date", help='Manager Birthdate')
    is_present = fields.Boolean(string='is_present')
    salary = fields.Float(string='Salary')

    employee_ids = fields.One2many('company.employee', 'manager_id', string='Employee')

    project_id = fields.Many2one('company.project', string='Project')
    project_ids = fields.Many2many('company.project', string='Other Projects')

    department_id = fields.Many2one('company.department', string='Department')


    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')




