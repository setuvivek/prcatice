# -*- coding: utf-8 -*-
from odoo import models,fields,api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class SetuElectronicItem(models.Model):
    _name = 'setu.electronic.item'
    _description = 'Setu Electronic Item'
    # _inherit = 'mail.thread', 'mail.activity.mixin'

    #Char-------------------------------
    name = fields.Char(string='Name')
    description = fields.Char(string='Description')

    #Integer-----------------------------
    code = fields.Integer(string='Code')

    #Float-------------------------------
    price = fields.Float(string='Unit Price')
    quantity = fields.Float(string='Product Quantity')
    total_price = fields.Float(string='Total Price')

    #Datetime----------------------------
    manufacture_date = fields.Datetime(string='Manufacture Date')
    warranty = fields.Datetime(string='Warranty')

    #Boolean-----------------------------
    is_it_predefined = fields.Boolean(string='PreDefined For Repair')

    #M2o---------------------------------
    company_id = fields.Many2one('setu.company',string='Company')


    #api_onchange--------------------------
    @api.onchange('manufacture_date')
    def onchange_manufacture_date(self):
        for rec in self:
            if rec.manufacture_date:
                rec.warranty = rec.manufacture_date + relativedelta(years=1)
            else:
                rec.warranty = False

    @api.onchange('quantity')
    def onchange_total_price(self):
        for rec in self:
            if rec.quantity:
                rec.total_price = rec.quantity * rec.price
            else:
                rec.total_price = False

    def copy(self, default=None):
        default = dict(default or {})
        if 'name' not in default:
            default['name'] = str(self.name) + "(copy)"
            default['code'] = self.code + 1
        return super(SetuElectronicItem, self).copy(default=default)
                
    





