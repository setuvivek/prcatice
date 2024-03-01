from datetime import datetime

from odoo import fields, models

class Student(models.Model):
    _name = "student"
    _description = "Student"
    # _rec_name = "gender"
    # _order = 'age desc'

    name = fields.Char(string='Student Name' ,default="hareeey",help="helppppppppppppppppppppppppp")
    age = fields.Integer(string='Age',copy=False)
    address = fields.Char(string='Address')
    gender = fields.Selection(selection = [("female","Female"),("male","Male")],string="Gender")
    family_member = fields.Integer(string='Member Of Family')
    studying_hour = fields.Float(string='Study Time')
    graduation = fields.Boolean(string='Graduate')
    date = fields.Date(string="Todays Date",default=datetime.now().strftime('%Y-%m-%d'))
    DateTime = fields.Datetime(string="Datetime",default=datetime.now())
    teacher_id = fields.Many2one("teacher",string='Teacher') #showing in table column and using group by teacher filter
    teacher_ids = fields.Many2many("teacher",string="Math Teachers" ,help="#table name:-select * from student_teacher_rel; (automatic generate)")
                                            #table name:-select * from student_teacher_rel; (automatic generate)

    teacher_science_ids = fields.Many2many("teacher","science_teacher_rel","student_id","teacher_id",string="Physics Teacher",help="#select * from science_teacher_rel; (we have to create manually because only one table is cretaed automatically by odoo taht's we have seen above)")
                                                    #select * from science_teacher_rel; (we have to create manually because only one table is cretaed automatically by odoo taht's we have seen above)
