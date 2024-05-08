# -*- coding: utf-8 -*-
from odoo import models,fields,api
from odoo.exceptions import ValidationError

class Customer(models.Model):
    _name = 'company.customer'
    _description = 'company.customer'


    #Char-----------------
    name = fields.Char(string='Name')
    street = fields.Char(string='Street')
    zip = fields.Char(string='Zip')
    address = fields.Char(string='Address')

    #Selection-------------
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender', default='female')

    #Date------------------
    dob = fields.Date(string="Birth Date", help='Customer BirthDate')

    #O2m-------------------
    project_ids = fields.One2many('company.project', 'customer_id', string='Project')


    #M2o-------------------
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')

    #Contrains-------------
    @api.constrains('name')
    def name_required(self):
        for record in self:
            if not record.name:
                raise ValidationError("Please enter name")

    # @api.constrains('project_ids')
    # def check_unique_project(self):
    #     for record in self:
    #         existing_project = self.search([('project_ids', '=', record.project_ids), ('id', '!=', record.id)])
    #         if existing_project:
    #             raise ValidationError("Project already exists.....")
