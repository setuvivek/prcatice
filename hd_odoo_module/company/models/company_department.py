# -*- coding: utf-8 -*-
from odoo import models, fields


class ComapnyDepartment(models.Model):
    _name = 'company.department'
    _description = 'company.department'

    name = fields.Char(string='Name', help='Department Name')

    manager_ids = fields.One2many('company.manager', 'department_id', string='Manager')
    employee_ids = fields.One2many('company.employee', 'department_id', string='Employee')
