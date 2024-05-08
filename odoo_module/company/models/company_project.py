# -*- coding: utf-8 -*-
from odoo import models, fields

class CompanyProject(models.Model):
    _name = 'company.project'
    _description = 'company.project'

    #Char----------------
    name = fields.Char(string='Name')
    definition = fields.Char(string='Project Definition')

    #M2o------------------
    customer_id = fields.Many2one('company.customer',string='Customer')

    #O2m------------------
    manager_ids = fields.One2many('company.manager', 'project_id', string='Manager')
    employee_ids = fields.One2many('company.employee', 'project_id', string='Employee')

