from  odoo import fields,models

class SetuMotherToungue(models.Model):
    _name = "setu.mother.tongue"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name",tracking=True)

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('name_unique', 'unique(name)', "Name Must Be Unique."),
    ]