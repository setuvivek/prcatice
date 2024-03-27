# -*- coding: utf-8 -*-
from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class SetuElectronicItem(models.Model):
    _name = 'setu.electronic.item'
    _description = 'Setu Electronic Item'

    #Char-------------------------------
    name = fields.Char(string='Name')
    description = fields.Char(string='Description')
    brand = fields.Char(string='Brand')

    #Integer-----------------------------
    code = fields.Integer(string='Code')

    #Float-------------------------------
    price = fields.Float(string='Price')

    #Datetime----------------------------
    manufacture_date = fields.Datetime(string='Manufacture Date')
    warranty = fields.Datetime(string='Warranty')

    #Boolean-----------------------------
    is_it_predefined = fields.Boolean(string='PreDefined For Repair')
    
    #Python Constrains-------------------
    @api.constrains
    def unique_code(self):
        for rec in self:
            existing_code = self.search([('code', '=', rec.code), ('id', '!=', rec.id)])
            if existing_code:
                raise ValidationError('This code already exists....')


    #api_onchange--------------------------
    @api.onchange('manufacture_date')
    def onchange_manufacture_date(self):
        for rec in self:
            if rec.manufacture_date:
                rec.warranty = rec.manufacture_date + relativedelta(years=1)
            else:
                rec.warranty = False
                
    





