from odoo import fields,models

class SetuStandardDivision(models.Model):
    _name = "setu.standard.division"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
    ]