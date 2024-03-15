from odoo import fields, models


class Teacher(models.Model):
    _name = "setu.teacher"
    _description = "setu_teacher"

    standard_id = fields.Many2one("setu.standard.standard", string="Responsibility of Academic Class")
    subject_ids = fields.Many2many("setu.subject", string="Subjects")
    school_id = fields.Many2one("setu.school", string="School")
    student_ids = fields.One2many("setu.student", 'teacher_id', string="Student")
    name = fields.Char(string="Teacher Name", required=True)
    active = fields.Boolean(string="Active", default=False)
    # WorkAddress(Stree, City, State, Country, zip, phone, email)
    work_address_street = fields.Char(string="Work Address")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    country_id = fields.Many2one("country",string="Country")
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

    def write(self, vals):
        rec = super(Teacher, self).write(vals)

        if 'active' in vals:

            active = vals.get('active')
            if not active:
                self.student_ids.mapped('school_id').write({'country_id': False})
                self.student_ids.write({'medium_id': False})
                self.student_ids.write({'first_name': False, 'gender': False, 'dob': False, 'blood_group':False, 'weight': False, 'height': False, 'state': False, 'terminate_reason': False, 'address': False})
            if active:
                # rec = self.env['setu.standard.standard'].search([('name', '=', self.standard_id)])
                # if rec:

                a = self.env['setu.student'].search([('roll_no', '=', '13')], limit=1)
                self.student_ids.write({'medium_id': a.medium_id})
                self.student_ids.mapped('school_id').write({'country_id': self.country_id.id})
                self.student_ids.write({'first_name': a.first_name, 'gender': a.gender, 'dob': a.dob, 'blood_group': 'AB+', 'weight': '50kg', 'height': '170cm', 'state': 'gujrat', 'terminate_reason': 'Go to other school', 'address': self.home_address_street})

                # self.student_ids.write({'first_name': 'rajj', 'gender': 'male', 'dob': '2002-02-02', 'blood_group': 'AB+', 'weight': '50kg','height':'170cm','state':'gujrat','terminate_reason':'Go to other school', 'address': self.home_address_street})

            #     a.write({'admission_date': '2025-02-22'})
            #     self.student_ids.mapped('school_id').write({'country_id': self.country})

        return rec
