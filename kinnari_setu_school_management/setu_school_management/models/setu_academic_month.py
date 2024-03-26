from odoo import fields,models, api,_
from odoo.exceptions import ValidationError


class SetuAcademicMonth(models.Model):
    _name = "setu.academic.month"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
    date_start = fields.Date(string="Start Date")
    date_stop = fields.Date(string="Stop Date")
    academic_year_id = fields.Many2one('setu.academic.year',string="Year")





    # _sql_constraints = [
    #     # Partial constraint, complemented by unique index (see below). Still
    #     # useful to keep because it provides a proper error message when a
    #     # violation occurs, as it shares the same prefix as the unique index.
    #     ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
    #     ('name_unique', 'unique(name)', "Name Must Be Unique."),
    #     ('code', 'CHECK(code>0)', 'Code cannot be negative.'),
    # ]

    @api.constrains('date_start', 'date_stop')
    def _constrains_dates_(self):
        for rec in self:
            if rec.date_start and rec.date_stop and rec.date_start > rec.date_stop:
                raise ValidationError(_('The stop date cannot be earlier than the start date. ',))

    def copy(self, default=None):
        default = dict(default or {})
        default['code'] = self.code + 1
        return super(SetuAcademicMonth, self).copy(default=default)
    #
    # @api.constrains('code')
    # def _check_code_(self):
    #     if not self.code:
    #         raise ValidationError(_('Missing code'))
