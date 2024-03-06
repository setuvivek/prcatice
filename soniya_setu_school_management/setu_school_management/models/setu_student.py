from odoo import api, models, fields

class Student(models.Model):
    _name = "setu.student"
    _description = "Student"

    name = fields.Char(string='Name')
    address = fields.Selection(selection=[('rajkot', 'Rajkot'), ('ahemdabad', 'Ahemdabad')], string='Address')
    email = fields.Char(string='email')
    phone = fields.Integer(string='Phone')
    roll_no = fields.Integer(string="Roll No")
    dob = fields.Date(string='Date Of Birth')
    teacher_ids = fields.Many2many('setu.teacher', string="Teacher")
    class_teacher_id = fields.Many2one('setu.teacher', string='Class Teacher')
    subject_ids = fields.Many2many('setu.subject', string='Subject')
    school_id = fields.Many2one('setu.school', string='School')
    # sci_teacher = fields.Many2many("teacher", "stu_teacher_subject", 'student_id', 'teacher_id', string="Sci_Teacher")


