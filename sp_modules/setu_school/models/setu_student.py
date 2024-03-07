from odoo import fields, models


class SetuStudent(models.Model):
    _name = 'setu.student'
    _description = 'Student'

    first_name = fields.Char(string='First Name', require=True)
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    dob = fields.Datetime(string='Birthdate')
    phone = fields.Char(string='Phone')
    email = fields.Text(string='Email')
    mobile = fields.Char(string='Mobile')
    bloodgroup=fields.Selection(selection=[('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'),('O+','O+'),('O-','O-')], string='Blood Group')
    weight=fields.Integer(string='Weight')
    height = fields.Integer(string='Height')
    address = fields.Text(string='Address')
    city_id = fields.Many2one('city',string='City')
    state_id = fields.Many2one('city',string='State')
    terminate_reason=fields.Char(string='Terminate Reason')
    active=fields.Boolean(string='Active')
    standard_id=fields.Many2one('setu.standard.standard',string='Standard')
    division_id = fields.Many2one('setu.standard.division', string='Division')
    medium_id=fields.Many2one('setu.standard.medium',string='Medium')
    school_id = fields.Many2one('setu.school', string='School ID')
    admission_date=fields.Datetime(string='Admission Date')
    academic_year_id=fields.Many2one('setu.academic.year',string='Academic Year')
    caste_id=fields.Many2one('setu.student.caste',string='Caste')
    mother_tongue=fields.Many2one('setu.mother.tongue',string='Mothertongue')
    roll_no = fields.Integer(string='Roll No.')
    class_id = fields.Many2one('setu.class', string='Class')
    class_teacher_id = fields.Many2one('setu.teacher', string='Class Teacher ID')
    teacher_ids = fields.Many2many('setu.teacher', 'student_teacher_ids', string='Teacher IDs')
    subject_ids = fields.Many2many('setu.subject', 'student_subjects', string='Subject IDs')
