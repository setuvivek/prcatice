from odoo import fields, models

class Teacher(models.Model):
    _name = "setu.teacher"
    _description = "setu_teacher"


    standard_id = fields.Many2one("setu.standard.standard", string="Responsibility of Academic Class")
    subject_ids = fields.Many2many("setu.subject", string="Subjects")
    school_id = fields.Many2one("setu.school", string="School")
    student_ids = fields.Many2many("setu.student",string="Student")
    name = fields.Char(string="Teacher Name", required=True)
    # WorkAddress(Stree, City, State, Country, zip, phone, email)
    work_address_street = fields.Char(string="Work Address")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    country = fields.Char(string="Country")
    zip = fields.Integer(string="zip")
    phone = fields.Char(string="phone")
    email = fields.Char(string="email")
    # Home Address(Stree, City, State, Country, zip, phone, email)
    home_address_street = fields.Char(string="Home Address")
    home_address_city = fields.Char(string="City")
    home_address_state = fields.Char(string="State")
    home_address_country = fields.Char(string="Country")
    home_address_zip = fields.Integer(string="zip")
    home_address_phone = fields.Char(string="phone")
    home_address_email = fields.Char(string="email")