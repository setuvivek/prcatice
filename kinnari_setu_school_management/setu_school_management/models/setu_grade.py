from  odoo import fields,models

class SetuGrade(models.Model):
    _name = "setu.grade"

    name = fields.Char(string="Name")
    grade_line_ids = fields.One2many('setu.grade.line','grade_id', string="Grade Lines")

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
    ]