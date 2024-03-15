# -*- coding: utf-8 -*-
from odoo import models,fields,api

class Employee(models.Model):
    _name = 'company.employee'
    _description = 'company.employee'



    #Char----------------------
    name = fields.Char(string='Name', required=True)
    address = fields.Char(string='Address')
    street = fields.Char(string='Street')
    zip = fields.Char(string='Zip')

    #Integer---------------------
    code = fields.Integer(string='Code', copy=False)

    #Selection-------------------
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender', default='female')

    #Date------------------------
    dob = fields.Date(string="Birth Date", help='Employee BirthDate')

    #Datetime--------------------
    join_date = fields.Datetime(string='Joining Date', help='Employee Join Date')

    #Boolean---------------------
    is_present = fields.Boolean(string='is_present')

    #Float-----------------------
    salary = fields.Float(string='Salary')

    #M2o-------------------------
    manager_id = fields.Many2one('company.manager', string='Manager')
    project_id = fields.Many2one('company.project', string='Project')
    department_id = fields.Many2one('company.department', string='Department')

    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')


    #create and search-----------
    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            record = self.env['company.manager'].search([('project_id', '=', vals.get('project_id')),
                                                          ('department_id', '=', vals.get('department_id'))], limit=1)
            if record:
                vals.update({'manager_id':record.id})

        res = super(Employee, self).create(vals_list)
        return res


