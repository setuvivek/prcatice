import datetime
from odoo import fields, models , api
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = "student"
    _description = "Student"
    _rec_name = "gender"
    _order = "roll"

    name = fields.Char(string="Name", )
    roll = fields.Integer(string="Roll", copy =False)
    gender = fields.Selection(selection=[('male','Male'),('female','Female')], string="Gender")
    dobs = fields.Date(string='Today Date')
    teach_id = fields.Many2one('teacher',string="Select Teacher")
    teacher1_id = fields.Many2many('teacher','teacher1',string="Maths Teacher")
    teacher2_id = fields.Many2many('teacher','teacher2', string="Science Teacher")
    teacher3_id = fields.Many2many('teacher', 'teacher3', string="Physics Teacher")
    enter1 = fields.Float(string="Maths Mark")
    enter2 = fields.Float(string="Science Mark")
    enter3 = fields.Float(string="Physics Mark")
    com = fields.Float(string="Total", compute="_abc",store=True)
    quantity = fields.Float(string="Quantity for order", copy=False)
    stock = fields.Boolean(string="Stock available or not", default=True)
    country_id = fields.Many2one('country', string="Country Name")
    state_id = fields.Many2one('state', string="State Name")
    city_id = fields.Many2one('city', string="City Name")

    @api.depends('enter1','enter2','enter3')
    def _abc(self):
        for record in self:
            record.com = record.enter1 + record.enter2 + record.enter3

    _sql_constraints = [
        ('name', 'unique(name)', 'Name Must Be Unique.'),
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('roll_unique' ,'unique(roll)', 'Roll Must Be Unique.' ),
        ('roll', 'CHECK(roll > 0)', 'roll no must be greater than 0.'),
        # ('check_name', "CHECK( (type='male' AND name IS NOT NULL)  )", 'require a name'),
        ('check_mark', 'CHECK(enter1 >= 0 AND enter1 <= 100)','mark should be between 0 and 100'),

    ]


    def write(self,vals):
        record = self.env['teacher'].search([('postgraduate','=',True),('gender','=','female'),('result','>=',60.0)])
        if record:
            vals.update({'teach_id':record.id})
        rec = super(Student,self).write(vals)
        return rec

    # @api.constrains('dobs')
    # def _check_dob(self):
    #
    #     current_date = (datetime.today()).strftime("%Y-%m-%d")
    #
    #     c_date = datetime.strptime(current_date, "%Y-%m-%d").date()
    #
    #     for record in self:
    #
    #         d_date = datetime.strptime(record.dobs, "%Y-%m-%d").date()
    #
    #         if c_date <= d_date:
    #             raise ValidationError("Your DOB is should be less then today date")


