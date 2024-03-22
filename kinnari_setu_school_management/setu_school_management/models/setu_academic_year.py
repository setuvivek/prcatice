from datetime import date, timedelta
import random
from datetime import datetime, date
from datetime import datetime
from dateutil.relativedelta import relativedelta, MO



from odoo import fields,models

class SetuAcademicYear(models.Model):
    _name = "setu.academic.year"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string="Name")
    code = fields.Integer(string="Code")
    date_start = fields.Date(string="Start Date")
    date_stop = fields.Date(string="Stop Date")
    month_ids = fields.One2many('setu.academic.month','academic_year_id' , string="Academic Month")





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
                # rec_id = self.env['setu.academic.year'].search([('date_start', '=', '2024-04-04')])
                # if rec_id:
                #     rec_id.write({'date_start': '2024-04-15'})

            rec = self.env['setu.academic.month'].search([('academic_year_id','=',self.id)])
            if rec:
                rec.write({'date_start':'2024-03-03'})









































                # record = self.env['setu.academic.year'].search([])
                # print(record)

                #
                # record_id = self.env['setu.academic.month'].search([('date_stop', '=', '2024-08-08')])
                # if record_id:
                #     record_id.write({'date_stop': '2024-08-08'})





























































