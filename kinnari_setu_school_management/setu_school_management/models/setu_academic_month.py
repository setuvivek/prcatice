from odoo import fields,models

class SetuAcademicMonth(models.Model):
    _name = "setu.academic.month"

    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
    date_start = fields.Date(string="Start Date")
    date_stop = fields.Date(string="Stop Date")
    academic_year_id = fields.Many2one('setu.academic.year',string="Year")

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('code', 'CHECK(code>=0)', 'Code cannot be negative.'),
    ]