from odoo import fields,models,api

class SetuStandardDivision(models.Model):
    _name = "setu.standard.division"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name",tracking=True)
    code = fields.Char(string="Code",tracking=True)
    is_div = fields.Boolean(string="Is Division?")

    # _sql_constraints = [
    #     # Partial constraint, complemented by unique index (see below). Still
    #     # useful to keep because it provides a proper error message when a
    #     # violation occurs, as it shares the same prefix as the unique index.
    #     ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
    #     ('name_unique', 'unique(name)', "Name Must Be Unique."),
    # ]

    def default_get(self, fields):
        res = super(SetuStandardDivision, self).default_get(fields)
        res.update({'code': 1})
        return res

    def copy(self, default=None):
        default = dict(default or {})
        default['code'] = self.code + "copy"
        return super(SetuStandardDivision, self).copy(default=default)






