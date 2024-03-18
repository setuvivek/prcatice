from odoo import models, fields, api
from datetime import timedelta, datetime

class SetuAcademicMonth(models.Model):
    _name = "setu.academic.month"
    _description = "SetuAcademicMonth"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    date_start = fields.Datetime(string="Start Date")
    date_stop = fields.Datetime(string="Stop Date")
    academic_year_id = fields.Many2one("setu.academic.year", string="Year")















