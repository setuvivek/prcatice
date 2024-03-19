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
    gender = fields.Selection(selection=[('male','Male'),('female','Female'),('other','Other')], string="Gender")
    add = fields.Char(string="add gender")
    dobs = fields.Date(string='Today Date')
    teach_id1 = fields.Many2one('teacher',string="Select Teacher")
    teach_id2 = fields.Many2one('teacher',string="Select Teacher")
    teach_id3 = fields.Many2one('teacher', string="Select Teacher")
    teach_id4 = fields.Many2one('teacher', string="Select Teacher")
    teach_id5 = fields.Many2one('teacher', string="Select Teacher")
    teacher1_id = fields.Many2many('teacher','teacher1',string="Maths Teacher")
    teacher2_id = fields.Many2many('teacher','teacher2', string="Science Teacher")
    teacher3_id = fields.Many2many('teacher', 'teacher3', string="Physics Teacher")
    enter1 = fields.Float(string="Maths Mark")
    enter2 = fields.Float(string="Science Mark")
    enter3 = fields.Float(string="Physics Mark")
    com = fields.Float(string="Total", compute="_abc",store=True)
    quantity = fields.Float(string="Quantity for order", copy=False)
    stock = fields.Boolean(string="Stock available or not", default=True)

    address = fields.Boolean(string="You want to add Resident Location")
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
        ('check_mark', 'CHECK(enter1 >= 0 AND enter1 <= 100)','mark should be between 0 and 100'),

    ]

    def write(self,vals):
        if not vals.get('teach_id'):
            rec = self.env['teacher'].search([('postgraduate','=',True)])
            if rec:
                vals.update({'teach_id':rec.id})
            res = super(Student,self).write(vals)
            return res



    # def write(self,vals):
    #     record = self.env['teacher'].search([('postgraduate','=',True),('gender','=','female'),('result','>=',60.0)])
    #     if record:
    #         vals.update({'teach_id':record.id})
    #     rec = super(Student,self).write(vals)
    #     return rec


    
   

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


