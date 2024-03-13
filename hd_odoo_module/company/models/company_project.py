# -*- coding: utf-8 -*-
from odoo import models, fields

class CompanyProject(models.Model):
    _name = 'company.project'
    _description = 'company.project'

    name = fields.Char(string='Name')
    definition = fields.Char(string='Project Definition')

    customer_id = fields.Many2one('company.customer',string='Customer')

    manager_ids = fields.One2many('company.manager', 'project_id', string='Manager')
    employee_ids = fields.One2many('company.employee', 'project_id', string='Employee')

