from datetime import date, timedelta
import random
from datetime import datetime, date
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO

from odoo.exceptions import ValidationError


from odoo import fields,models, _

class SetuAcademicYear(models.Model):
    _name = "setu.academic.year"

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
    date_start = fields.Date(string="Start Date")
    date_stop = fields.Date(string="Stop Date")
    month_ids = fields.One2many('setu.academic.month','academic_year_id' , string="Academic Month")

    # j = date_start
    # k = j + relativedelta(months=-1)
    # l = k.strftime('%Y')
    # current = fields.Integer(k)



    def action_create(self):
            self.month_ids.unlink()
            a = self.date_start
            b = self.date_stop

            while a<=b:

                a = a + relativedelta(months=1)
                x = a + relativedelta(months=-1)
                y = a + relativedelta(months=0,days=-1)

                self.env['setu.academic.month'].create({"name":x.strftime('%B'),
                                                        "code":self.code,
                                                        "date_start": x,
                                                        "date_stop": y,
                                                        "academic_year_id": self.id})

    # def unlink(self):
    #     for record in self:
    #         if record.start_date:
    #             raise ValidationError(_('Eroor'))
    #     res = super(SetuAcademicYear , self).unlink()
    #     return res






















  #
  # record[("x_studio_month")] = datetime.record.x_studio_from.strftime("%B")

































































