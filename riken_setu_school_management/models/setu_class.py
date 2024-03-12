from odoo import models, fields

class SetuClass(models.Model):
    _name = "setu.class"
    _description = "SetuClass"
    _rec_name = "name"

    name = fields.Char(string="name")
    class_teacher_id = fields.Many2one("setu.teacher", string="Class Teacher")
    teacher_ids = fields.Many2many("setu.teacher", string="Teacher")
    student_ids  = fields.Many2many("setu.student", "class_student" "class" "student",string="Student")
    school_id = fields.Many2one("setu.school", string="School")
    subject_ids = fields.Many2many("setu.subject", "class_subject" "class" "subject", string="Subject")