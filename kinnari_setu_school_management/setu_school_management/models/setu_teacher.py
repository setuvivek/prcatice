from odoo import fields, models,api

class SetuTeacher(models.Model):
    _name = "setu.teacher"

    name = fields.Char(string="Name" , required=True , copy=False)
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    email = fields.Char(string="Email")
    mobile = fields.Char(string="mobile" , help="Enter mobile Number" , size=10)
    phone = fields.Char(string="Phone", help="Enter Phone Number" , size=10)
    standard_id = fields.Many2one('setu.class', string="Responsibility of Academic Class")
    subject_ids = fields.Many2many('setu.subject', 'setu_teachers_subjects', string="Subject")
    school_id = fields.Many2one('setu.school' , string="Campus")
    student_ids = fields.Many2many('setu.student','setu_teachers_students' , string="Students")
    home_address = fields.Char(string="Home Address")
    street = fields.Char(string="Street")
    country = fields.Char(string="Country")
    zip = fields.Char(string="ZIP")



    # Stree, City, State, Country, zip, phone, email

    @api.model
    def create(self, vals_list):
        if not vals_list.get('phone'):
            vals_list.update({'phone': '281'})
        res = super(SetuTeacher, self).create(vals_list)
        return res

