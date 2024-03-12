from odoo import fields, models,api, _
from odoo.exceptions import ValidationError

class SetuTeacher(models.Model):
    _name = "setu.teacher"

    name = fields.Char(string="Name")
    address = fields.Char(string="Address")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    email = fields.Char(string="Email")
    mobile = fields.Char(string="mobile" , help="Enter mobile Number" , size=10)
    phone = fields.Char(string="Phone", help="Enter Phone Number" , size=10)
    standard_id = fields.Many2one('setu.class', string="Responsibility of Academic Class")
    division_id = fields.Many2one('setu.standard.division', string="Division")
    medium_id = fields.Many2one('setu.standard.medium', string="Medium")
    school_id = fields.Many2one('setu.school', string="Campus")
    subject_ids = fields.Many2many('setu.subject', 'setu_teachers_subjects', string="Subject")
    student_ids = fields.One2many('setu.student','teacher_id', string="Students")
    home_address = fields.Char(string="Home Address")
    street = fields.Char(string="Street")
    country = fields.Char(string="Country")
    zip = fields.Char(string="ZIP")
    is_teacher = fields.Boolean(string="Is teacher")



    # Stree, City, State, Country, zip, phone, email

    @api.model
    def create(self, vals_list):
        if not vals_list.get('phone'):
            vals_list.update({'phone': '281'})
        res = super(SetuTeacher, self).create(vals_list)
        return res


    _sql_constraints = [
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('name_unique', 'unique(name)', "Name Must Be Unique."),
    ]

    @api.constrains('zip')
    def _verify_zip(self):
        for rec in self:
            if rec.zip and not rec.zip.isdigit():
                raise ValidationError(_("The zip must be a sequence of digits."))
