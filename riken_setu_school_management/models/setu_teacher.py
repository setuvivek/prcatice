from odoo import models, fields

class SetuTeacher(models.Model):
    _name = "setu.teacher"
    _description = "SetuTeacher"
    _rec_name = "name"

    standard_id = fields.Many2one("setu.standard.standard", string="Responsibility of Academic Class")
    subject_ids = fields.Many2many("setu.subject", string="Subjects")
    school_id = fields.Many2one("setu.school", string="Campus")
    student_ids = fields.Many2many("setu.student", "student_teacher" "student" "teacher", string="Student")
    name = fields.Char(string="Name")
    work_city_id = fields.Many2one("city", string="Work City")
    work_state_id = fields.Many2one("state", string="Work State")
    work_country_id = fields.Many2one("country", string="Work Country")
    home_city_id = fields.Many2one("city", string="Home City")
    home_state_id = fields.Many2one("state", string="Home State")
    home_country_id = fields.Many2one("country", string="Home Country")