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

    def write(self,vals_list):
        # vals_list = {'name':'hemangi'}
        vals_list = {}
        res = super(SetuAcademicYear, self).write(vals_list)
        return res

        # res = super('setu.academic.year').unlink()
        # for record in self.month_ids:
        #     if record.date_start:
        #         raise ValidationError("Not Delete")
        #     record.unlink()
        # return res








