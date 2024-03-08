from odoo import api, models, fields

class Student(models.Model):
    _name = "setu.student"
    _description = "Student"

    first_name = fields.Char(string='First Name')
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    date_of_birth = fields.Date(string='DOB')
    blood_group = fields.Char(string='Blood Group')
    weight = fields.Integer(string='Weight')
    height = fields.Integer(string='Height')
    state = fields.Char(string='State')
    terminate_reason = fields.Char(string='Terminate Reason')
    active = fields.Boolean(string='Active')
    standard_id = fields.Many2one('setu.class', string='Class')
    division_id = fields.Many2one('setu.standard.division', string='Division')
    medium_id = fields.Many2one('setu.standard.medium', string='Medium')
    school_id = fields.Many2one('setu.school', string='School')
    admission_date = fields.Date(string='Admission Date')
    academic_year_id = fields.Many2one('setu.academic.year', string='Year')
    roll_no = fields.Integer(string='Roll No')
    cast_id = fields.Many2one('setu.student.cast', string='Cast')
    mother_toungue_id = fields.Many2one('setu.mother.toungue', string='Mothe Toungue')
    # class_teacher_id = fields.Many2one('setu.teacher', string='Teacher')



