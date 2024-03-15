from odoo import fields, models, api
from odoo.exceptions import MissingError, ValidationError, AccessError

class Teacher(models.Model):
    _name = "teacher"
    _description = "Teacher"
    # _rec_name = "name" #je rakhie te file upar setting ni bajuma show kare as a description
    # _order = "gender"

    # _order = 'sequence, id'

    name = fields.Char(string='Teacher name')
    age = fields.Integer(string='Age')
    standard = fields.Integer(string='Standard')
    gender = fields.Selection(selection = [("female","Female"),("male","Male")],string="Gender")
    subject = fields.Selection(selection = [("maths","Maths"),("physics","Physics"),("chemistry","Chemistry"),("biology","Biology")],string="Teaching Subject")
    student_ids = fields.One2many("student","teacher_id",string="Student",help="this is reference of teacher table")  #we have to add new data in this & already buit in(we have to select) data in Many2many
    department_id = fields.Many2one("department",string="Department")
    active = fields.Boolean(string="Active" ,default='True')
    city_id = fields.Many2one("city", string="City")


    _sql_constraints = [
        ("age",
         "CHECK(age>30)",
         "age is not grater than 18"),
    ]


