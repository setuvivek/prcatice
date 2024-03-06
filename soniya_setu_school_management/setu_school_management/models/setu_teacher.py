from odoo import models, fields

class Teacher(models.Model):

    _name = "setu.teacher"
    _description = "Setu_Teacher"

    name = fields.Char(string='Name')
    address = fields.Selection(selection=[('rajkot', 'Rajkot'),('baroda', 'Baroda')], string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='email')
    mobile = fields.Char(string='Mobile')
    school_id = fields.Many2one("setu.school", string='School')
    subject_id = fields.Many2one("setu.subject", string='Subject')
    student_ids = fields.One2many('setu.student','class_teacher_id', string='Students')
    class_ids = fields.One2many('setu.class','class_teacher_id', string='Class')