from odoo import api, fields, models
from datetime import *
from dateutil.relativedelta import relativedelta

import calendar
from odoo.exceptions import MissingError, ValidationError, AccessError


class Academic_year(models.Model):
    _name = "setu.academic.year"
    _description = "setu_academic_year"

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Name", required=True)
    code = fields.Char(string='Code')
    date_start = fields.Date(string="Date Start")
    date_stop = fields.Date(string="Date Stop")
    month_ids = fields.One2many("setu.academic.month", "academic_year_id", string="Academic Month")
    current = fields.Char(string="Active Academic", compute ='_compute_current_date')

    def _compute_current_date(self):
        for rec in self:
            stah = rec.date_start + relativedelta(months=1)
            rec.current = stah.strftime("%Y")


    def action_done(self):
        self.month_ids.unlink()  # new record add thay juno delete thay
        start = self.date_start
        stop = self.date_stop
        j = []
        while start <= stop:
            start += relativedelta(months=1)
            sta = start + relativedelta(months=-1)

            j.append({"name": sta.strftime("%B"),
                      "code": sta.strftime("%b"),
                      "date_start": start + relativedelta(months=-1),
                      "date_stop": start + relativedelta(months=0, days=-1),
                      "academic_year_id": self.id})
            # j = []
            # j = [{"name": start.strftime("%B"), "date_start": start + relativedelta(months=-1),
            #       "date_stop": start + relativedelta(months=0, days=-1),
            #       "academic_year_id": self.id}]
        self.env['setu.academic.month'].create(j)

    def write(self, vals):
        # self.env['setu.academic.month'].search([('date_start','>','2023-12-01'),('date_stop', '<', '2024-06-30'),('code','=','123')])
        rec = self.env['setu.academic.month'].search([('date_start', '=', '2024-04-01')])
        print(rec)
        # if rec:
        #     raise ValidationError("found")



        if not vals.get('code'):
            vals.update({'code': '111'})

        res = super(Academic_year, self).write(vals)
        # u = self.month_ids.browse(self.month_ids.ids)
        return res

    # def unlink(self):

    # for record_id in self:

    # record_id.unlink()
    # if record_id.date_start:
    #     raise ValidationError(("Not Delete."))
    # print("RECORD%s" % self)
    # res = super(Academic_year, self).unlink()
    # return res
