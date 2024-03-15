from datetime import datetime

from odoo.exceptions import ValidationError
from odoo import api, fields, models


class Student(models.Model):
    _name = "student"
    _description = "Student"
    # _rec_name = "gender"
    # _order = 'age desc'

    name = fields.Char(string='Student Name', default="hareeey", help="helppppppppppppppppppppppppp")
    age = fields.Integer(string='Age')
    address = fields.Char(string='Address')
    city_id = fields.Many2one("city", string="City")
    gender = fields.Selection(selection=[("female", "Female"), ("male", "Male"), ("a", "A"), ("b", "B"), ("c", "C")],
                              string="Gender")
    family_member = fields.Integer(string='Member Of Family')
    studying_hour = fields.Float(string='Study Time')
    graduation = fields.Boolean(string='Graduate')
    date = fields.Date(string="Todays Date", default=datetime.now().strftime('%Y-%m-%d'))
    DateTime = fields.Datetime(string="Datetime", default=datetime.now())
    teacher_id = fields.Many2one("teacher",
                                 string='Teacher')  # showing in table column and using group by teacher filter
    teacher_ids = fields.Many2many("teacher", string="Math Teachers",
                                   help="#table name:-select * from student_teacher_rel; (automatic generate)")
    # table name:-select * from student_teacher_rel; (automatic generate)

    teacher_science_ids = fields.Many2many("teacher", "science_teacher_rel", "student_id", "teacher_id",
                                           string="Physics Teacher",
                                           help="#select * from science_teacher_rel; (we have to create manually because only one table is cretaed automatically by odoo taht's we have seen above)")
    standard = fields.Integer(string="Standard")
    degree = fields.Selection(selection=[('it','IT'),('finance','Finance'),('other','Other')], string="Degree")
    other_degree = fields.Char(string="Other")

    # select * from science_teacher_rel; (we have to create manually because only one table is cretaed automatically by odoo taht's we have seen above)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('address'):
                vals['address'] = 'addresssssss'
        # if not vals_list.get('gender'):
        #     vals_list.update({'gender': 'male'})
        res = super(Student, self).create(vals_list)
        res.gender = 'male'

        return res

    # @api.model
    # def create(self, vals):
    #
    #     if not vals.get('address'):
    #         vals.update({'address':'addresssss'})
    #     # if not vals_list.get('gender'):
    #     #     vals_list.update({'gender': 'male'})
    #     res = super(Student, self).create(vals)
    #     res.gender = 'male'
    #
    #     return res

    def write(self, vals):
        rec = self.env['teacher'].search(['&', ('active', '=', True), ('standard', '=', 4)], limit=1)
        if rec:
            vals.update({'teacher_id': rec.id})
            vals.update({'graduation': True})
            vals.update({'teacher_science_ids': [(0, 0, {'name': rec.name, 'age': rec.age, 'standard': rec.standard, 'gender': rec.gender, 'subject': rec.subject, 'department_id': rec.department_id})]})

        res = super(Student, self).write(vals)
        return res

    # @api.model_create_multi
    # def create(self, vals_list):
    #     for val in vals_list:
    #         val['address'] = 'addresssssss'
    #
    #     res = super(Student, self).create(vals_list)
    #     return res
