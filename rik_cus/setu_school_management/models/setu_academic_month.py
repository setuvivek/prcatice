from odoo import models, fields, api
from datetime import timedelta, datetime

class SetuAcademicMonth(models.Model):
    _name = "setu.academic.month"
    _description = "SetuAcademicMonth"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    code = fields.Char(string="Code", tracking = True)
    date_start = fields.Datetime(string="Start Date", tracking = True)
    date_stop = fields.Datetime(string="Stop Date", tracking = True)
    academic_year_id = fields.Many2one("setu.academic.year", string="Year")















