from odoo import fields, models


class Teacher(models.Model):
    _name = "setu.teacher"
<<<<<<< HEAD
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender",tracking=True)
    postgraduate = fields.Boolean(string="Have Master Degree?")
    master = fields.Selection(selection=[('maths','maths'),('physics','physics'),('chemistry','chemistry'),('biology','biology'),('other','other')],string="Master In")
    add = fields.Char(string="Write about it")
    sure = fields.Boolean(string="Are you want to add Personal details?")
    email = fields.Char(string="Email")
    mobile = fields.Char(string="mobile" , help="Enter mobile Number" , size=10)
    phone = fields.Char(string="Phone", help="Enter Phone Number" , size=10)
    standard_id = fields.Many2one('setu.class', string="Responsibility of Academic Class")
    division_id = fields.Many2one('setu.standard.division', string="Division")
    medium_id = fields.Many2one('setu.standard.medium', string="Medium")
    school_id = fields.Many2one('setu.school', string="Campus")
    subject_ids = fields.Many2many('setu.subject', 'setu_teachers_subjects', string="Subject")
    student_ids = fields.One2many('setu.student','teacher_id', string="Students")
    is_teacher = fields.Boolean(string="Is teacher")
    address = fields.Boolean(string="Are You want to add  Home Address?")
    city_id = fields.Many2one('city', string="City Name")
    state_id = fields.Many2one('state', string="State Name")
    country_id = fields.Many2one('country', string="Country Name")
    zip = fields.Char(string="zip")
=======
    _description = "setu_teacher"

    standard_id = fields.Many2one("setu.standard.standard", string="Responsibility of Academic Class")
    subject_ids = fields.Many2many("setu.subject", string="Subjects")
    school_id = fields.Many2one("setu.school", string="School")
    student_ids = fields.One2many("setu.student", 'teacher_id', string="Student")
    name = fields.Char(string="Teacher Name", required=True)
    age = fields.Integer(string='Age')
    mini_age_ofschool = fields.Integer(related="school_id.required_age")
    active = fields.Boolean(string="Active", default=False)
    code_of_school = fields.Integer(string="Code", compute='_compute_code_of_school', readonly=False)
>>>>>>> 0c53dcac5aa5f8ad5e4668828bd4bbe6b6c4ec57

    # WorkAddress(Stree, City, State, Country, zip, phone, email)
    work_address_street = fields.Char(string="Work Address")
    city = fields.Char(string="City")
    state = fields.Char(string="State")
    country_id = fields.Many2one("country", string="Country")
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

    def _compute_code_of_school(self):
        # self.code_of_School = 10
        for rec in self:
            if self.school_id:
                rec.code_of_school = rec.school_id.code
            # rec.code_of_school = rec.zip

    def write(self, vals):
        rec = super(Teacher, self).write(vals)

        if 'active' in vals:

            active = vals.get('active')
            if not active:
                self.student_ids.mapped('school_id').write({'country_id': False})
                self.student_ids.write({'medium_id': False})
                # self.student_ids.write({'first_name': False, 'gender': False, 'dob': False, 'blood_group':False, 'weight': False, 'height': False, 'state': False, 'terminate_reason': False, 'address': False})
            if active:
                a = self.env['setu.student'].search([('roll_no', '=', '13'), ('school_id', '=', self.school_id)])
                if a:
                    a.write({'teacher_id': self.id})

                # a = self.env['setu.student'].search([('roll_no', '=', '13')], limit=1)
                # self.student_ids.write({'medium_id': a.medium_id})
                # self.student_ids.mapped('school_id').write({'country_id': self.country_id.id})
                # self.student_ids.write({'first_name': a.first_name, 'gender': a.gender, 'dob': a.dob, 'blood_group': 'AB+', 'weight': '50kg', 'height': '170cm', 'state': 'gujrat', 'terminate_reason': 'Go to other school', 'address': self.home_address_street})

        return rec
