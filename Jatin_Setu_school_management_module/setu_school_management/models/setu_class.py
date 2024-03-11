from odoo import fields, models

class Class(models.Model):
    _name = "setu.class"

    _description = "setu_class"

    name = fields.Char(string="Class Name" , required=True)
    class_teacher_id = fields.Many2one("setu.teacher",string="Class Teacher")
    teacher_ids = fields.Many2many("setu.teacher","class_teacher_table",string="Teacher")
    student_ids = fields.Many2many("setu.student","class_student_table", string="Student")
    school_ids = fields.Many2many("setu.school","class_school_table", string="School")
    subject_ids = fields.Many2many("setu.subject","class_subject_table", string="Subject")



