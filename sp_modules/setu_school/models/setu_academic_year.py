from odoo import fields, models, _

from dateutil import rrule
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError, UserError


def convert_to_datetime(input_str, parserinfo=None):
    return parse(input_str, parserinfo=parserinfo)


class SetuAcademicYear(models.Model):
    _name = 'setu.academic.year'
    _description = 'academic year'

    sequence = fields.Integer(string='sequence')
    name = fields.Char(string='name')
    code = fields.Char(string='code')
    date_start = fields.Date(string='Start Date')
    date_stop = fields.Date(string='End Date')
    month_ids = fields.One2many('setu.academic.month', 'academic_year_id', string='Months')

    # current = fields.Selection(selection=[('one', 'One'), ('two', 'Two')], string='status')

    def month_list(self):
        list = []
        for dt in rrule.rrule(rrule.MONTHLY, dtstart=self.date_start, until=self.date_stop):
            ld = dt + relativedelta(day=31)
            list.append(
                {"name": dt.strftime("%B"), "date_start": dt.strftime("%Y-%m-%d"), "date_stop": ld.strftime("%Y-%m-%d"),
                 'academic_year_id': self.id})
        self.env['setu.academic.month'].create(list)
    def clear_list(self):
        self.month_ids.unlink()
    # def unlink(self):
    #     print("RECORD%s" % self)
    #     res = super(SetuAcademicYear, self).unlink()
    #     return res


class SetuAcademicMonth(models.Model):
    _name = 'setu.academic.month'
    _description = 'Academic Month'

    name = fields.Char(string='name')
    code = fields.Char(string='code')
    date_start = fields.Datetime(string='Start Date')
    date_stop = fields.Datetime(string='End Date')
    academic_year_id = fields.Many2one('setu.academic.year', string='Academic Year')

    # def unlink(self):
    #     print("RECORD%s" % self)
    #     res = super(SetuAcademicMonth, self).unlink()
    #     return res