from odoo import models, fields


class AcademicMonth(models.Model):

    _name = "setu.academic.month"
    _description = "Setu_Academic_Month"


    name = fields.Char(string='Name')
    code = fields.Char(string='Code')
    date_start = fields.Date(string='Start Date')
    date_stop = fields.Date(string='End date')
    academic_year_id = fields.Many2one('setu.academic.year', string='Date')
    #month_ids = fields.One2many

