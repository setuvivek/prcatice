from odoo import models, fields


class Student(models.Model):
    _name = "student"
    _description = "Student"
    # _rec_name = "department"

    name = fields.Char(string='Name', required=True)
    age = fields.Char(string='Age', required=True, default=20)
    department = fields.Selection(
        selection=[('CE', 'CE'), ('IT', 'IT'), ('Civil', 'Civil'), ('Mechanical', 'Mechanical'),
                   ('Bio Technology', 'Bio Technology')], string='Department')
    roll_no = fields.Integer(string="Roll No", copy=False)
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    hobby = fields.Boolean(string="Store Data")
    dob = fields.Date(string='Date Of Birth')
    teacher_id = fields.Many2one("teacher", string="Teacher")
    teacher_ids = fields.Many2many("teacher", string="Subject Teacher")
    sci_teacher = fields.Many2many("teacher", "stu_teacher_subject", 'student_id', 'teacher_id', string="Sci_Teacher")
