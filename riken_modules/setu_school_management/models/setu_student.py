from odoo import models, fields, api
from odoo.exceptions import ValidationError
class SetuStudent(models.Model):
    _name ="setu.student"
    _description = "SetuStudent"
    _rec_name = "first_name"


    first_name = fields.Char(string="First Name", help="Student Name")
    middle_name = fields.Char(string="Middle Name", help="Father Name")
    last_name = fields.Char(string="Last Name", help="Surname")
    gender = fields.Selection(selection=[("male","MALE"),("female","FEMALE")], string="Gemder")
    dob = fields.Date(string="DOB")
    blood_group = fields.Char(string="Blood Group",required=True)
    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height")
    state = fields.Char(string="State", default='Saurashtra')
    terminate_reason = fields.Char(string="Terminate Reason")
    active = fields.Boolean(string="Active", default='True')
    address = fields.Char(string="Address")
    standard_id = fields.Many2one("setu.standard.standard", string="Class")
    division_id = fields.Many2one("setu.standard.division", string="Division")
    medium_id = fields.Many2one("setu.standard.medium", string="Medium")
    school_id = fields.Many2one("setu.school", string="School")
    admission_date = fields.Date(string="Admission Date")
    academic_year_id = fields.Many2one("setu.academic.year", string="Year")
    roll_no = fields.Integer(string="Roll_no")
    cast_id = fields.Many2one("setu.student.cast", string="Cast")
    mother_tongue_id = fields.Many2one("setu.mother.tongue", string="Mother Tongue")
    class_teacher_id = fields.Many2one("setu.teacher", string="Class Teacher")

    @api.constrains('dob')
    def check_dob(self):
        for rec in self:
            if rec.dob and rec.dob > fields.Date.today():
                raise ValidationError("The entered date is not acceptable")

    def update_rollno(self):
        self.search([('first_name', '=', 'riken')]).write({'first_name':'Riken'})




        # self.env['setu.student'].update_rollno()

    # record_m_ids = self.env['setu.academic.month'].search([('academic_year_id', '=', self.id)])
    # if record_m_ids:
    #     record_m_ids.write({'date_start': '2026-09-01'})

    # self.env['crm.stage'].search([]).write({'sequence': 9999})