from odoo import fields, models

class Teacher(models.Model):
    _name = "setu.teacher"
    _description = "setu_teacher"

    name = fields.Char(string="Teacher Name" , required=True)
    address = fields.Char(string="Address")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")
    mobile = fields.Char(string="Mobile No.")
    school_id = fields.Many2one("setu.school", string="School")
    subject_id = fields.Many2one("setu.subject", string="Subject")
    student_ids = fields.One2many("setu.student","class_teacher_id",string="Student")
    class_ids = fields.One2many("setu.class","class_teacher_id",string="Class")


