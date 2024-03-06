from odoo import api,fields, models
from datetime import *
from dateutil.relativedelta import *

import calendar


class Academic_month(models.Model):
    _name = "setu.academic.month"
    _description = "setu_academic_month"


    name = fields.Char(string="Month")
    code = fields.Char(string='Code')
    date_start = fields.Date(string="Date Start")
    date_stop = fields.Date(string="Date Stop")
    academic_year_id = fields.Many2one("setu.academic.year",string="Year")
