from odoo import models, fields

class Teacher(models.Model):

    _name = "setu.teacher"
    _description = "Setu_Teacher"

    # name = fields.Char(string='Name')
    # address = fields.Selection(selection=[('rajkot', 'Rajkot'),('baroda', 'Baroda')], string='Address')
    # phone = fields.Char(string='Phone')
    # email = fields.Char(string='email')
    # mobile = fields.Char(string='Mobile')
    # school_id = fields.Many2one("setu.school", string='School')
    # subject_id = fields.Many2one("setu.subject", string='Subject')
    # # student_ids = fields.One2many('setu.student','class_teacher_id', string='Students')
    # class_ids = fields.One2many('setu.class','class_teacher_id', string='Class')

    standard_id = fields.Many2one('setu.standard.standard', string='Responsibility of Academic Class')
    subject_ids = fields.Many2many('setu.subject', string='Subjects')
    school_id = fields.Many2one('setu.school', string='Campus')
    student_ids = fields.Many2many('setu.student', string='Students')
    name = fields.Char(string='Name')

    work_address = fields.Char(string="work address")
    # home_address = fields.Char(string="home address")
    # street = fields.Char(string='Street')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    country = fields.Char(string='Country')
    zip = fields.Char(string='Zip')
    phone = fields.Integer(string='Phone')
    email = fields.Char(string='Email')

    home_address = fields.Char(string="home address")
    city1 = fields.Char(string='City')
    state1 = fields.Char(string='State')
    country1 = fields.Char(string='Country')
    zip1 = fields.Char(string='Zip')
    phone1 = fields.Integer(string='Phone')
    email1 = fields.Char(string='Email')
