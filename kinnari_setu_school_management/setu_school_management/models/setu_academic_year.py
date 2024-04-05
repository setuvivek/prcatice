from odoo import api, fields, models
from datetime import *
from dateutil.relativedelta import relativedelta

import calendar
from odoo.exceptions import MissingError, ValidationError, AccessError


class Academic_year(models.Model):
    _name = "setu.academic.year"
<<<<<<< HEAD
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

    def copy(self, default=None):
        default = dict(default or {})
        default['sequence'] = self.sequence + 1
        return super(SetuAcademicYear, self).copy(default=default)




































                # record = self.env['setu.academic.year'].search([])
                # print(record)

                #
                # record_id = self.env['setu.academic.month'].search([('date_stop', '=', '2024-08-08')])
                # if record_id:
                #     record_id.write({'date_stop': '2024-08-08'})





























































=======
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
>>>>>>> 0c53dcac5aa5f8ad5e4668828bd4bbe6b6c4ec57
