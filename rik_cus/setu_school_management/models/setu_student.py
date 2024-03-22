from odoo import models, fields, api
from odoo.exceptions import ValidationError
class SetuStudent(models.Model):
    _name ="setu.student"
    _description = "SetuStudent"
    _rec_name = "first_name"
    _inherit = ['mail.thread','mail.activity.mixin']


    first_name = fields.Char(string="First Name", help="Student Name", tracking=True)
    middle_name = fields.Char(string="Middle Name", help="Father Name", tracking=True)
    last_name = fields.Char(string="Last Name", help="Surname", tracking=True)
    gender = fields.Selection(selection=[("male","MALE"),("female","FEMALE")], string="Gender")
    dob = fields.Date(string="DOB", tracking=True)
    blood_group = fields.Char(string="Blood Group",required=True)
    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height")
    state = fields.Char(string="State", default='Saurashtra')
    terminate_reason = fields.Char(string="Terminate Reason")
    active = fields.Boolean(string="Active", default='True')
    address = fields.Char(string="Address", tracking=True)
    standard_id = fields.Many2one("setu.standard.standard", string="Class")
    division_id = fields.Many2one("setu.standard.division", string="Division")
    medium_id = fields.Many2one("setu.standard.medium", string="Medium")
    school_id = fields.Many2one("setu.school", string="School")
    admission_date = fields.Date(string="Admission Date")
    academic_year_id = fields.Many2one("setu.academic.year", string="Year")
    roll_no = fields.Integer(string="Roll_no", tracking=True)
    cast_id = fields.Many2one("setu.student.cast", string="Cast", tracking=True)
    mother_tongue_id = fields.Many2one("setu.mother.tongue", string="Mother Tongue")
    class_teacher_id = fields.Many2one("setu.teacher", string="Class Teacher")
    class_teacher_phone = fields.Integer(string='Teacher Phone', compute="_compute_teacher_phone", store=True)
    class_teacher_email = fields.Char(string='Teacher Email', compute="_compute_teacher_information")

    @api.depends('class_teacher_id')
    def _compute_teacher_phone(self):
        for rec in self:
            if rec.class_teacher_id:
                rec.class_teacher_phone = rec.class_teacher_id.phone
            else:
                rec.class_teacher_phone = False

    def _compute_teacher_information(self):
        for rec in self:
            if rec.class_teacher_id:
                rec.class_teacher_email = rec.class_teacher_id.email
            else:
                rec.class_teacher_email = False


    @api.depends('class_teacher_id')
    def _compute_teacher_information(self):
        for rec in self:
            if rec.class_teacher_id:
                rec.class_teacher_phone = rec.class_teacher_id.phone
            else:
                rec.class_teacher_phone = False

    def _compute_teacher_email(self):
        for rec in self:
            if rec.class_teacher_id:
                rec.class_teacher_email = rec.class_teacher_id.email
            else:
                rec.class_teacher_email = False






















    #
    # @api.constrains('first_name')
    # def _check_unique_student_name(self):
    #     for record in self:
    #         existing_student = self.env['setu.student'].search([('first_name', 'ilike', record.first_name)])
    #         if len(existing_student) > 1 or (len(existing_student) == 1 and existing_student[0] != record):
    #             raise ValidationError(f'Student name "{record.first_name}" already exists!')

    # @api.constrains('dob')
    # def check_dob(self):
    #     for rec in self:
    #         if rec.dob and rec.dob > fields.Date.today():
    #             raise ValidationError("The entered date is not acceptable")

    # def update_rollno(self):
    #
    #         rec = self.env['student'].search([('standard', '=', 4)], limit=1)
    #         if rec:
    #             rec.write({'teacher_id': rec.id})
    # @api.model_create_multi
    # def create(self, values):
    #     new_student = super(SetuStudent, self).create(values)
    #     return new_student
    #
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            class_teacher_rec = self.env['setu.teacher'].search([
                ('class_teacher', '=', 'True'),
                ('standard_id', '=', vals.get('standard_id')),
                ('medium_id', '=', vals.get('medium_id')),
                ('division_id', '=', vals.get('division_id'))
            ], limit=1)

            if class_teacher_rec:
                vals.update({'class_teacher_id': class_teacher_rec.id})

        res = super(SetuStudent, self).create(vals_list)
        return res

    def write(self, vals):
        if 'standard_id' in vals or 'medium_id' in vals or 'division_id' in vals:
            current_record = self[0]

            class_teacher_rec = self.env['setu.teacher'].search([
                ('class_teacher', '=', 'True'),
                ('standard_id', '=', vals.get('standard_id', current_record.standard_id.id)),
                ('medium_id', '=', vals.get('medium_id', current_record.medium_id.id)),
                ('division_id', '=', vals.get('division_id', current_record.division_id.id))
            ], limit=1)

            if class_teacher_rec:
                vals.update({'class_teacher_id': class_teacher_rec.id})

        res = super(SetuStudent, self).write(vals)
        return res



    #     class_teacher_rec = self.env['setu.teacher'].search(['|', '|',
    #         ('standard_id', '=', vals.get('standard_id')),
    #         ('class_teacher', '=', 'True'),
    #         ('medium_id', '=', vals.get('medium_id')),
    #         ('division_id', '=', vals.get('division_id'))
    #     ])
    #     if class_teacher_rec:
    #         vals.update({'class_teacher_id': class_teacher_rec[0].id})
    #
    #     res = super(SetuStudent, self).write(vals)
    #     return res

    # domain = [
    #     '|', ('class_teacher', '=', 'True'), ('standard_id', '=', vals.get('standard_id')),
    #     ('medium_id', '=', vals.get('medium_id'))
    # ]
    # def write(self, vals):
    #     rec = self.env['setu.teacher'].search([('standard_id', '=', '10')], limit=1)
    #     if rec:
    #         vals.update({'class_teacher_id': rec.id})
    #     res = super(SetuStudent, self).write(vals)
    #     return res
        # self.search([('first_name', '=', 'riken')]).write({'first_name':'Riken'})
    # def create
    #     if rec:
    #         vals.update({"class_teacher_id": rec.id})
    #     res = super(Set



        # self.env['setu.student'].update_rollno()

    # record_m_ids = self.env['setu.academic.month'].search([('academic_year_id', '=', self.id)])
    # if record_m_ids:
    #     record_m_ids.write({'date_start': '2026-09-01'})

    # self.env['crm.stage'].search([]).write({'sequence': 9999})

