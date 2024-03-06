# -*- coding: utf-8 -*-
from odoo import models, fields, api
import calendar
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta


class SetuAcademicYear(models.Model):
    _name = 'setu.academic.year'
    _description = 'Academic Year'

    sequence = fields.Integer(string='Sequence')
    name = fields.Char(string='Name')
    code = fields.Integer(string='Code')
    date_start = fields.Date(string='Date Start')
    date_stop = fields.Date(string='date Stop')
    current = fields.Char(string='Active Academic')
    month_ids = fields.One2many('setu.academic.month', 'academic_year_id', string='Academic Month')

    # def action_done(self):
    #     vals = [{"name": "JULY", "date_start": "2024-01-03", "date_stop": "2025-01-03","academic_year_id": self.id}]
    #     self.env['setu.academic.month'].create(vals)
    #     pass

    def action_done(self):
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



        # start_date = self.date_start
        # end_date = self.date_stop
        #
        # if start_date <= end_date:
        #     start_date += relativedelta(months=0)
        #     end_date += relativedelta(months=0)
        #
        # self.env['setu.academic.month'].create({
        #         'date_start':start_date,
        #         'date_stop':end_date,
        #         'academic_year_id': self.id,
        #     })



        # vals = []
        # date_start = fields.Date.from_string(self.date_start)
        # date_stop = fields.Date.from_string(self.date_stop)
        #
        # current_date = date_start
        # while current_date <= date_stop:
        #
        #     vals.append(current_date.strftime('%B'))
        #     current_date += relativedelta(months=1)
        #
        # print(vals)
        # for i in vals:
        #     self.env['setu.academic.month'].create({
        #         'name': i,
        #         'academic_year_id': self.id,
        #     })


    # current_month = self.date_start.month
    # current_year = self.date_start.year
    # current_day = self.date_start.day
    #
    #
    # while current_year < self.date_stop.year or (current_year == self.date_stop.year and current_month <= self.date_stop.month):
    #     months = fields.Date.to_string(fields.Date.from_string(f'{current_year}-{current_month}-{current_day}'))
    #
    #     vals.append(months)
    #
    #     current_month += 1
    #     if current_month > 12:
    #         current_month = 1
    #         current_year += 1
    #
    # for month in vals:
    #     self.env['setu.academic.month'].create({
    #         'date_start': month,
    #         'academic_year_id': self.id,
    #     })
    #     print(month)

# @api.model_create_multi
# def create(self, vals_list):
#     res = super(SetuAcademicYear, self).create(vals_list)
#     return res
#

# def action_done(self):
#     vals = []
#
#     start_date = fields.Date.from_string(self.date_start)
#     end_date = fields.Date.from_string(self.date_start)
#
#     current_date = start_date
#     while current_date <= end_date:
#         vals.append(current_date.strftime('%B'))
#         current_date = relativedelta(months=+1)
#         print(vals)





# from odoo import models, fields, api
# from dateutil.relativedelta import relativedelta
#
# class AcademicMonth(models.Model):
#     _name = 'academic.month'
#     _description = 'Academic Month'
#
#     name = fields.Char(string='Month', required=True)
#     start_date = fields.Date(string='Start Date', required=True)
#     end_date = fields.Date(string='End Date', required=True)
#     academic_year_id = fields.Many2one('school.year', string='Academic Year')
#
# class SchoolYear(models.Model):
#     _name = 'school.year'
#     _description = 'School Year'
#
#     name = fields.Char(string='Year', required=True)
#     start_date = fields.Date(string='Start Date', required=True)
#     end_date = fields.Date(string='End Date', required=True)
#     academic_month_ids = fields.One2many('academic.month', 'academic_year_id', string='Academic Months')
#
#     @api.multi
#     def generate_report(self):
#         # Create academic months
#         current_date = self.start_date
#         while current_date < self.end_date:
#             next_date = current_date + relativedelta(months=1)
#             month_name = current_date.strftime('%B %Y')
#             self.env['academic.month'].create({
#                 'name': month_name,
#                 'start_date': current_date,
#                 'end_date': next_date - relativedelta(days=1),
#                 'academic_year_id': self.id,
#             })
#             current_date = next_date
#
#         # Print the list of months
#         print("List of academic months:")
#         for month in self.academic_month_ids:
#             print(month.name)

