from odoo import models, fields, api
import datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class SetuAcademicYear(models.Model):
    _name = "setu.academic.year"
    _description = "SetuAcademicYear"

    sequence = fields.Char(string="Sequence")
    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
    date_start = fields.Datetime(string="Start Date")
    date_stop = fields.Datetime(string="Stop Date")
    month_ids = fields.One2many("setu.academic.month", "academic_year_id", string="Month")
    current = fields.Integer(string="Active Academic")


    def action_done(self):
        # for record_id in self:
        #     if record_id.date_start:
        #         raise ValidationError("Not Delete.")
        start_date = self.date_start
        end_date = self.date_stop
        months = []
        self.month_ids.unlink()

        while start_date <= end_date:
            start_date += relativedelta(months=1)
            sta = start_date + relativedelta(months=-1)

            months.append({
                'name': sta.strftime('%B'),
                'code': sta.strftime('%b'),
                'date_start': start_date + relativedelta(months=-1),
                'date_stop': start_date + relativedelta(months=0, days=-1),
                'academic_year_id': self.id
            })


        self.env["setu.academic.month"].create(months)
        record_m_ids = self.env['setu.academic.month'].search([('academic_year_id', '=', self.id)])
        if record_m_ids:
            record_m_ids.write({'date_start':'2026-09-01'})

    # def unlink(self):
    #
    #     print("RECORD%s" % self)
    #     res = super(SetuAcademicYear, self).unlink()
    #     return res


    #     vals = [{"date_start": self.date_start, "date_stop": self.date_stop, "academic_year_id": self.month_ids}]
    #     self.env['setu.academic.month'].create(vals)

    def write(self, vals):
        # print(vals)
        # vals = {"code":"552"}
        res = super(SetuAcademicYear, self).write(vals)
        return res