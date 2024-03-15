# -*- coding: utf-8 -*-
from odoo import models,fields

class Manager(models.Model):
    _name = 'company.manager'
    _description = 'company.manager'

    #Char------------------
    name = fields.Char(string='Name', required=True)
    street = fields.Char(string='Street')
    zip = fields.Char(string='Zip')
    address = fields.Char(string='Address')

    #Integer-----------------
    code = fields.Integer(string='Code', copy=False)

    #Selection---------------
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender', default='female')

    #Date--------------------
    dob = fields.Date(string="Birth Date", help='Manager Birthdate')

    #Boolean-----------------
    is_present = fields.Boolean(string='is_present')

    #Float-------------------
    salary = fields.Float(string='Salary')

    #O2m---------------------
    employee_ids = fields.One2many('company.employee', 'manager_id', string='Employee')

    #M2o---------------------
    project_id = fields.Many2one('company.project', string='Project')
    department_id = fields.Many2one('company.department', string='Department')

    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')

    #M2m---------------------
    project_ids = fields.Many2many('company.project', string='Other Projects')




