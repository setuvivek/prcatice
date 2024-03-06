from odoo import api, models, fields
from datetime import datetime
from dateutil.relativedelta import relativedelta

class AcademicYear(models.Model):

    _name = "setu.academic.year"
    _description = "Setu_Academic_Year"

    sequence = fields.Integer(string="Sequence")
    name = fields.Char(string='Name')
    code = fields.Integer(string='Code')
    date_start = fields.Date(string='Start Date')
    date_stop = fields.Date(string='End date')
    current = fields.Date(string='Date')
    # month_ids = fields.One2many('setu.academic.month', 'academic_year_id', string='Days')
    month_ids = fields.One2many('setu.academic.month', 'academic_year_id', string='Days')


    def action_done(self):
        date_star = self.date_start
        date_end = self.date_stop
        # vals=[]
        while date_star <= date_end:
            date_star += relativedelta(months=+1)
            nme = date_star + relativedelta(months=-1)
            vals=[]

            # vals = [{'name': nme.strftime("%B"),
            #          'code': nme.strftime("%b"),
            #          'date_start': date_star + relativedelta(months=-1),
            #          'date_stop': date_star + relativedelta(months=0, days=-1),
            #          'academic_year_id': self.id}]

            vals.append({'name': nme.strftime("%B"),
                         'code': nme.strftime("%b"),
                         'date_start': date_star + relativedelta(months=-1),
                         'date_stop': date_star + relativedelta(months=0, days=-1),
                         'academic_year_id': self.id})

            self.env['setu.academic.month'].create(vals)

        # while date_star <= date_end:
        #     date_star += relativedelta(months=+1)
            # sta = date_star + relativedelta(months=-1)

            # vals = [{"name":'', "date_start": date_start.month , "date_end": date_end.month, },

        # vals = [{'name':date_star.month-1,
        #          'date_start':date_star + relativedelta(months=-1),
        #          'date_stop':date_star + relativedelta(months= 0, days=-1),
        #          'academic_year_id': self.id}]
        # vals = [{'name':self.name, 'date_start':dastart + relativedelta(months=-1), 'date_stop':date_start + relativedelta(months=0), 'academic_year_id':self.id}]

        # self.env['setu.academic.month'].create(vals)



    # res_dates = [date_start]
    # while date_start != date_stop:
    #     date_start += timedelta(days=1)
    #
    #     vals = [{'sequence'}]
    #     res_dates.append(date_start)

    # self.env['setu_academic_year'].create


    # def action_done(self):

        # @api.onchange('date_start', 'date_stop')
        # def month_ids(self):
        #     if self.date_start and self.date_stop:
        #         self.month_ids.unlink()
        #
        #         current_date = self.date_start
        #         while current_date <= self.date_stop:
        #             self.month_ids.create({'date':'current_date', 'month_ids':self.id})
        #             current_date += timedelta(day=1)


        # vals = [{"name": "JULY", "date_start": "2024-01-12", "date_stop": "2024-01-12", },
        #         {"name": "DEC", "date_start": "2024-01-12", "date_stop": "2024-01-12", },
        #         {"name": "NOV", "date_start": "2024-01-12", "date_stop": "2024-01-12", "academic_year_id": self.id}]
        # self.env['setu.academic.month'].create(vals)
        # pass

    # def dates_between(self, date_start, date_end, mode='date'):
    #     val = input("Enter start date: ")
    #     val1 = input("end date")
    #     delta = date_start - date_end
    #     if delta.days < 0:
    #         return None
    #
    #     res = []
    #     for i in range(delta.days+1):
    #         if mode == 'date':
    #             res.append(date_start + timedelta(days=i))

    # Python3 code to demonstrate working of
    # Random K dates in Range
    # Using choices() + timedelta() + loop

    # initializing dates ranges
    # test_date1, test_date2 = date(2015, 6, 3), date(2015, 7, 1)

    # printing dates
    # print("The original range : " + str(test_date1) + " " + str(test_date2))

    # initializing K
    # K = 7
    #
    # res_dates = [test_date1]

    # loop to get each date till end date
    # while test_date1 != test_date2:
    #     test_date1 += timedelta(days=1)
    #     res_dates.append(test_date1)

    # random K dates from pack
    # res = choices(res_dates, k=K)

    # printing
    # print("K random dates in range : " + str(res))









