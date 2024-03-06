from odoo import fields, models

class Student(models.Model):
    _name = "setu.student"
    _description = "setu_student"


    name = fields.Char(string="Student Name" , required=True)
    address = fields.Char(string="Address")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    roll_no = fields.Integer(string="Roll No.")
    dob = fields.Date(string="DOB")
    teacher_ids = fields.Many2many("setu.teacher",string="Teacher")
    class_teacher_id = fields.Many2one("setu.teacher",string="Teacher")
    subject_ids = fields.Many2many("setu.subject","student_subject_tab",string="Subject")
    school_id = fields.Many2one("setu.school",string="School")

