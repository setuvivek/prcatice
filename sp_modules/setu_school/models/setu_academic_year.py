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
        if self.date_start and self.date_stop:
            self.month_ids.unlink()
            list = []

            for dt in rrule.rrule(rrule.MONTHLY, dtstart=self.date_start, until=self.date_stop):
                lastday = dt + relativedelta(day=31)
                list.append(
                    {"name": dt.strftime("%B"), "date_start": dt.strftime("%Y-%m-%d"),
                     "date_stop": lastday.strftime("%Y-%m-%d"),  # "working_days": lastdt,
                     'academic_year_id': self.id})
            self.env['setu.academic.month'].create(list)
            record_m_ids = self.env['setu.academic.month'].search([('academic_year_id', '=', self.id)])
            if record_m_ids:
                record_m_ids.write({"date_start": "2026-05-01"})

        else:
            raise ValidationError(_("Select Start and End Dates"))

    def clear_list(self):
        self.month_ids.unlink()

    def unlink(self):
        for record_id in self:
            if record_id.date_start:
                raise ValidationError(_("Not Delete."))
        res = super(SetuAcademicYear, self).unlink()
        return res

    # def write(self, vals):
    #     # print(vals)
    #     # vals = {"code":"552"}
    #     res = super(SetuAcademicYear, self).write(vals)
    #     return res


class SetuAcademicMonth(models.Model):
    _name = 'setu.academic.month'
    _description = 'Academic Month'

    name = fields.Char(string='name')
    code = fields.Char(string='code')
    date_start = fields.Datetime(string='Start Date')
    date_stop = fields.Datetime(string='End Date')
    # working_days=fields.Date(string='Working Days',help='Sat-Sun Off')
    academic_year_id = fields.Many2one('setu.academic.year', string='Academic Year')
    product_id = fields.Many2one('product', string="Product")

    # def unlink(self):
    #     print("RECORD%s" % self)
    #     res = super(SetuAcademicMonth, self).unlink()
    #     return res

    # def write(self, vals):
    #     res = super(SetuAcademicMonth, self).write(vals)
    #     return res
