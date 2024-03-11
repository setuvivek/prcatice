from odoo import api,fields, models
from datetime import *
from dateutil.relativedelta import *

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
    month_ids = fields.One2many("setu.academic.month","academic_year_id",string="Academic Month")
    current = fields.Date(string="Active Academic")

    def action_done(self):

        self.month_ids.unlink() #new record add thay juno delete thay
        # NOW = datetime(2003, 9, 17, 20, 54, 47, 282310)
        # NOW = datetime.now()

        # TODAY = date.today()
        # vals = [{"name": NOW.month, "date_start": "2024-01-12", "date_stop": "2024-01-12", "academic_year_id": self.id}]
        start = self.date_start
        stop = self.date_stop

        # for i in range(start+relativedelta(months=+1),stop+relativedelta(months=+0)):
        #  i = [{"name": i,"code":self.code, "date_start": start, "date_stop": stop+relativedelta(months=-1), "academic_year_id": self.id}]
        #  self.env['setu.academic.month'].create(i)
        #
        # list = [start]
        j=[]
        while start <= stop:
            start += relativedelta(months=1)
            sta = start+relativedelta(months=-1)
            # list.append(start)
        # for i in range(start.month,stop.month):
        #     for j in i:
        #     if i == start.month+relativedelta(months=+1):
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
        # pass
        # else:
        #     print("ended")

    def unlink(self):
        for record_id in self:
            # record_id.unlink()
            if record_id.date_start:
                raise ValidationError(("Not Delete."))
        print("RECORD%s" % self)
        res = super(Academic_year, self).unlink()
        return res
