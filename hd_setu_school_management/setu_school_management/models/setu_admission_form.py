# -*- coding: utf-8 -*-
from odoo import models, fields


class SetuAdmissionForm(models.Model):
    _name = 'setu.admission.form'
    _description = 'Setu Admission Form'

    # Char
    student_name = fields.Char(string='Student Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')

    # date
    dob = fields.Date(string='DOB')

    #selection
    status = fields.Selection(selection=[('draft', 'Draft'), ('confirm', 'Confirm')], default='draft')

    # m2o
    class_id = fields.Many2one('setu.class', string='Class')
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')
