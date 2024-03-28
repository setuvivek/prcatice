# -*- coding: utf-8 -*-
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta
from odoo.exceptions import AccessError, MissingError, ValidationError, UserError


class SetuAcademicYear(models.Model):
    _name = 'setu.academic.year'
    _description = 'Academic Year'

    #Char.
    name = fields.Char(string='Name')
    current = fields.Char(string='Active Academic')


    #Integer
    code = fields.Integer(string='Code')
    sequence = fields.Integer(string='Sequence')

    #Boolean
    is_create = fields.Boolean(string='Create Month')

    #Date
    date_start = fields.Date(string='Date Start')
    date_stop = fields.Date(string='date Stop')

    #O2m
    month_ids = fields.One2many('setu.academic.month', 'academic_year_id', string='Academic Month')
    student_ids = fields.One2many('setu.student', 'academic_year_id', string='Year')

    # def action_done(self):
    #     vals = [{"name": "JULY", "date_start": "2024-01-03", "date_stop": "2025-01-03","academic_year_id": self.id}]
    #     self.env['setu.academic.month'].create(vals)
    #     pass

    def action_done(self):
        self.month_ids.unlink()
        list= []
        current_date = self.date_start
        while current_date < self.date_stop:
            next_date = current_date + relativedelta(months=1)
            month_name = current_date.strftime('%B')
            list.append({
                'name': month_name,
                'code': month_name[:3],
                'date_start': current_date,
                'date_stop': next_date - relativedelta(days=1),
                'academic_year_id': self.id,
            })
            current_date = next_date

        self.env['setu.academic.month'].create(list)

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         current_date = vals.get('date_start')
    #         while current_date < vals.get('date_stop'):
    #             next_date = current_date + relativedelta(months=1)
    #             month_name = current_date.strftime('%B')
    #     res = super(SetuAcademicYear, self).create(vals_list)
    #     return res



    def action_clear(self):
        self.month_ids.unlink()


        # record = self.env['setu.academic.month'].search([('academic_year_id', '=', self.id)])
        # if record:
        #     record.write({'date_start':'2026-05-01'})
        # else:
        #     raise ValidationError("this date does not exists...")

    def unlink(self):
        for record in self.month_ids:
            if record.date_start:
                raise ValidationError("Not Delete")
            record.unlink()



    def write(self,vals_list):
        record = vals_list.update({'code':self.code})
        if record:
            raise ValidationError('Code does not change!')

        # vals_list = {'code':self.code}
        # vals_list = {}
        res = super(SetuAcademicYear, self).write(vals_list)
        return res

    # #python constrains---------
    # @api.constrains('code')
    # def check_unique_code(self):
    #     for rec in self:
    #         existing_code = self.search([('code', '=', rec.code), ('id', '!=', rec.id)])
    #         if existing_code:
    #             raise ValidationError("code ust be unique..................")




# from odoo import models, fields, api
#
# class AllRequest(models.Model):
#     _name = 'all.request'
#     _description = 'All Requests'
#
#     repair_request_id = fields.Many2one('repair.request', string='Repair Request')
#
# class RepairRequest(models.Model):
#     _name = 'repair.request'
#     _description = 'Repair Requests'
#
#     item_id = fields.Many2one('electronics.item', string='Item', required=True)
#     description = fields.Text(string='Description')
#     status = fields.Selection([('new', 'New'), ('in_progress', 'In Progress'), ('completed', 'Completed')],
#                               string='Status', default='new')
#     date = fields.Date(string='Date', default=fields.Date.today())
#     customer_id = fields.Many2one('res.partner', string='Customer')
#     technician_id = fields.Many2one('res.partner', string='Technician')
#     priority = fields.Selection([('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], string='Priority', default='medium')
#     onhand = fields.Integer(string='Onhand', compute='_compute_onhand', store=True)
#
#     @api.depends('item_id')
#     def _compute_onhand(self):
#         for request in self:
#             request.onhand = self.env['repair.request'].search_count([('item_id', '=', request.item_id.id)])
#
#     def add_to_all_requests(self):
#         all_request_obj = self.env['all.request']
#         for request in self:
#             all_request_obj.create({'repair_request_id': request.id})


















# from odoo import models, fields, api
# from odoo.exceptions import ValidationError
#
# class RepairRequest(models.Model):
#     _name = 'repair.request'
#     _description = 'Repair Requests'
#
#     item_id = fields.Many2one('electronics.item', string='Item', required=True)
#     description = fields.Text(string='Description')
#     status = fields.Selection([('new', 'New'), ('in_progress', 'In Progress'), ('completed', 'Completed')],
#                               string='Status', default='new')
#     date = fields.Date(string='Date', default=fields.Date.today())
#     customer_id = fields.Many2one('res.partner', string='Customer')
#     technician_id = fields.Many2one('res.partner', string='Technician')
#     priority = fields.Selection([('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], string='Priority', default='medium')
#
    # @api.model
    # def create(self, vals):
    #     if 'item_id' in vals:
    #         existing_request = self.env['repair.request'].search([('item_id', '=', vals['item_id']), ('status', '=', 'in_progress')])
    #         if existing_request and existing_request.status != 'completed':
    #             raise ValidationError('The product is currently in repair. Cannot create another repair request.')
    #     return super(RepairRequest, self).create(vals)

