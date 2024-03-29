from  odoo import fields,models

class SetuStudentCast(models.Model):
    _name = "setu.student.cast"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('name_unique', 'unique(name)', "Name Must Be Unique."),
    ]