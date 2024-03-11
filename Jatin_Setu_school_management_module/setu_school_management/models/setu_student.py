from odoo import fields, models

class Student(models.Model):
    _name = "setu.student"
    _description = "setu_student"


    first_name = fields.Char(string="Name")
    middle_name = fields.Char(string="Middle Name")
    last_name = fields.Char(string="Last Name")
    address = fields.Char(string="Address")
    gender = fields.Selection(selection=[("female", "Female"), ("male", "Male")], string="Gender")
    dob = fields.Date(string="DOB")
    blood_group = fields.Char(string="Blood Group")
    weight = fields.Char(string="Weight")
    height = fields.Char(string="Height")
    state = fields.Char(string="State")
    terminate_reason = fields.Char(string="Terminate Reason")
    active = fields.Boolean(string="Active")
    standard_id = fields.Many2one("setu.standard.standard", string="Class")
    division_id = fields.Many2one("setu.standard.division", string="Division")
    medium_id = fields.Many2one("setu.standard.medium", string="Medium")
    school_id = fields.Many2one("setu.school", string="School")
    admission_date = fields.Date(string="Admission Date")
    academic_year_id = fields.Many2one("setu.academic.year",string="Year")
    roll_no = fields.Integer(string="Roll No.")
    cast_id = fields.Many2one("setu.student.cast",string="Cast")
    mother_tongue_id = fields.Many2one("setu.mother.tongue",string="Mother Tongue")
