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

    @api.model_create_multi
    def create(self, vals_list):
        res = super(SetuAcademicYear, self).create(vals_list)
        return res

    def write(self,vals_list):
        # record = {'code': self.code}
        # if record:
        #     raise ValidationError("can't update code!")

        vals_list = {'code':self.code}
        # vals_list = {}
        res = super(SetuAcademicYear, self).write(vals_list)
        return res

    # #python constrains---------
    # @api.constrains('code')
    # def check_unique_code(self):
    #     for rec in self:
    #         existing_code = self.search([('code', '=', rec.code), ('id', '!=', rec.id)])
    #         if existing_code:
    #             raise ValidationError("code ust be uniqueee..................")














