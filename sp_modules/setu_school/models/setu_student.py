from odoo import fields, models, api
from odoo.exceptions import ValidationError


class SetuStudent(models.Model):
    _name = 'setu.student'
    _description = 'Student'

    first_name = fields.Char(string='First Name', require=True)
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    dob = fields.Date(string='Birthdate')
    phone = fields.Char(string='Phone')
    email = fields.Text(string='Email')
    mobile = fields.Char(string='Mobile')
    bloodgroup = fields.Selection(
        selection=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'),
                   ('O-', 'O-')], string='Blood Group')
    weight = fields.Integer(string='Weight')
    height = fields.Integer(string='Height')
    caste_id = fields.Many2one('setu.student.caste', string='Caste')
    mother_tongue = fields.Many2one('setu.mother.tongue', string='Mothertongue')
    address = fields.Text(string='Address')
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('city', string='State')
    terminate_reason = fields.Char(string='Terminate Reason')
    active = fields.Boolean(string='Active', default='True')
    standard_id = fields.Many2one('setu.standard.standard', string='Standard')
    division_id = fields.Many2one('setu.standard.division', string='Division')
    medium_id = fields.Many2one('setu.standard.medium', string='Medium')
    school_id = fields.Many2one('setu.school', string='School ID')
    admission_date = fields.Date(string='Admission Date')
    academic_year_id = fields.Many2one('setu.academic.year', string='Academic Year')
    roll_no = fields.Integer(string='Roll No.')
    class_id = fields.Many2one('setu.class', string='Class')
    # class_teacher_id = fields.Many2one('setu.teacher', string='Class Teacher')
    class_teacher_id = fields.Many2one('setu.teacher', string='Class Teacher')
    alternate_id = fields.Many2one('setu.teacher', string='Alternate Teacher')
    teacher_ids = fields.Many2many('setu.teacher', 'student_teacher_ids', string='Teachers')
    subject_ids = fields.Many2many('setu.subject', 'student_subjects', string='Subjects')

    # ------------------------------------------------
    @api.model
    def create(self, vals):
        rec = self.env['setu.teacher'].search(
            [('class_teacher', '=', 'True'), ('standard_id', '=', vals.get('standard_id')),
             ('medium_id', '=', vals.get('medium_id')), ('division_id', '=', vals.get('division_id'))], limit=1)
        if rec:
            vals.update({"class_teacher_id": rec.id, "alternate_id": rec.id})
        res = super(SetuStudent, self).create(vals)
        return res

    # both works same:

    # @api.model
    # def create(self, vals):
    #     res = super(SetuStudent, self).create(vals)
    #     rec = self.env['setu.teacher'].search([('class_teacher', '=', 'True'), ('standard_id', '=', res.standard_id.id),('medium_id', '=', res.medium_id.id),('division_id', '=', res.division_id.id)], limit=1)
    #     if not res.class_teacher_id:
    #         res.class_teacher_id = rec.id
    #     return res
    # ------------------------------------------------

    @api.constrains('first_name', 'standard_id', 'division_id', 'medium_id')
    def check_not_null_name(self):
        for rec in self:
            if not (rec.first_name and rec.standard_id and rec.division_id and rec.medium_id):
                raise ValidationError("Required Deatils : \n\n Name,Code,Standard,Medium,Division")

    def assign(self):
        rec = self.env['setu.teacher'].search(
            [('class_teacher', '=', 'True'), ('standard_id', '=', self.standard_id.id),
             ('medium_id', '=', self.medium_id.id), ('division_id', '=', self.division_id.id)], limit=1)
        self.class_teacher_id = rec.id
