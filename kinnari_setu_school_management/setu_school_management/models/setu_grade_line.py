from odoo import fields,models

class SetuGradeLine(models.Model):
    _name = "setu.grade.line"

    from_mark = fields.Date(string="From Mark")
    to_mark = fields.Date(string="To Mark")
    name = fields.Char(string="Name")
    fail = fields.Boolean(string="Fail")
    grade_id = fields.Many2one('setu.grade' , string="Grade")

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
    ]