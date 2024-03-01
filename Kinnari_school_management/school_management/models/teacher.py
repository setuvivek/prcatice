from odoo import fields, models


class Teacher(models.Model):
    _name = "teacher"
    _description = "Teacher_details"
    # _rec_name = "mobile"
    _order = "result"

    # _date_name = 'date'

    name = fields.Char(string="Name", required=True)
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender")
    mobile = fields.Char(string="Mobileno", help="Enter Mobile Number", size=10)
    postgraduate = fields.Boolean(string="Postgraduate", default=False)
    result = fields.Float(string="Result", help="Enter result of Postgraduate", digit=(3,2))
    dob = fields.Date(string="Date of Birth", copy=False)
    student_id = fields.One2many('student','teach_id',string="Students")
    country_id = fields.Many2one('country', string="Country Name")
    state_id = fields.Many2one('state', string="State Name")
    city_id = fields.Many2one('city', string="City Name")
    priority = fields.Selection([

        ('clear', 'Clear'),

        ('urgent', 'Urgent'),

        ('normal', 'Normal'),

        ('lowand', 'Lowand'),

        ('high', 'High')],

        copy=False, default='normal', required=True)

    # department_id = fields.Many2many('department','dept1','name','name1',string="Department")






    # cunt = fields.Datetime.now()
    # cur = fields.Datetime(string="Current Date", default=lambda self: fields.Datetime.now())
