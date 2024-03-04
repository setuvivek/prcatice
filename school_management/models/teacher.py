from odoo import models, fields

class Teacher(models.Model):

    _name = "teacher"
    _description = "Teacher"
    _rec_name = "name"
    _order = "age desc"

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection(selection=[('male', 'MALE'), ('female', 'FEMALE')], string='Gender',default="male")
    age = fields.Integer(string='Age')
    phn_no = fields.Integer(string='Phn_No')
    city = fields.Char(string='City')
    joining_date = fields.Datetime(string="joining_date")
    student_ids = fields.One2many("student", "teacher_id", string="Student")
    department_ids = fields.One2many("department", "teacher_id", string="department")

    #department_id = fields.Many2one("department", string="department")