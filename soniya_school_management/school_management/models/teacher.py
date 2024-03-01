from odoo import models, fields


class Student(models.Model):
    _name = "teacher"
    _description = "teacher management"
    # _rec_name = "department"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age', required=True)
    department = fields.Selection(
        selection=[('CE', 'CE'), ('IT', 'IT'), ('Civil', 'Civil'), ('Mechanical', 'Mechanical'),
                   ('Bio Technology', 'Bio Technology')])
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')])
    subject = fields.Char(string="Subject")
    teacher_ids = fields.One2many('student', 'teacher_id', string='Subject')
    department_ids = fields.Many2one('department', string="Teacher")
    # subjects = fields.Many2many('teacher', string='Science_teacher')
