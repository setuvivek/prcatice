from odoo import models, fields

class SetuClass(models.Model):
    _name = "setu.class"
    _description = "SetuClass"
    _rec_name = "name"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="name", tracking=True)
    class_teacher_id = fields.Many2one("setu.teacher", string="Class Teacher", tracking=True)
    teacher_ids = fields.Many2many("setu.teacher", string="Teacher")
    student_ids  = fields.Many2many("setu.student", "class_student" "class" "student",string="Student")
    school_id = fields.Many2one("setu.school", string="School", tracking=True)
    subject_ids = fields.Many2many("setu.subject", "class_subject" "class" "subject", string="Subject")