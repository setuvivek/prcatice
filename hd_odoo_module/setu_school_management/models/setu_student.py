# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import AccessError, MissingError, ValidationError, UserError
from datetime import date

class SetuStudent(models.Model):
    _name = 'setu.student'
    _description = 'Setu Student'
    _inherit = 'mail.thread', 'mail.activity.mixin'

    # Char-------------
    first_name = fields.Char(string='First Name')
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name')
    address = fields.Char(string='Address')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    blood_group = fields.Char(string='Blood Group')
    terminate_reason = fields.Char(string='Terminate Reason')
    street = fields.Char(string='Street')
    zip = fields.Char(string='Zip')

    teacher_phone = fields.Char(string='Teacher Phone')
    teacher_email = fields.Char(string = 'Teacher Email')

    # Integer-------------
    roll_no = fields.Integer(string='Roll No')
    weight = fields.Integer(string='Weight')
    height = fields.Integer(string='Height')

    # Boolean------------
    active = fields.Boolean(string='Active', default=True)
    is_above_18 = fields.Boolean(string='Is Above 18', compute='_compute_is_above_18')

    # Selection-----------
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')])

    # Date----------------
    date_of_birth = fields.Datetime(string='DOB')

    # Datetime------------
    admission_date = fields.Datetime(string='Admission Date')

    # m2o-----------------
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')
    class_teacher_id = fields.Many2one('setu.teacher', string='Class Teacher')
    school_id = fields.Many2one('setu.school', string='School')
    standard_id = fields.Many2one('setu.class', string='Class')
    division_id = fields.Many2one('setu.standard.division', string='Division', tracking=True)
    medium_id = fields.Many2one('setu.standard.medium', string='Medium')
    academic_year_id = fields.Many2one('setu.academic.year', string='Year')
    mother_tongue_id = fields.Many2one('setu.mother.tongue', string='Mother Tongue')

    # m2m------------------
    teacher_ids = fields.Many2many('setu.teacher', 'student_teacher', 'student', 'teacher', string='Teacher')
    subject_ids = fields.Many2many('setu.subject', 'student_subject', 'student', 'subject', string='Subject')

    #related----------------
    teacher_subject = fields.Many2one(related='class_teacher_id.subject_id', store=True)


    #object button----------
    def action_done(self):
        record = self.env['setu.teacher'].search([('is_teacher', '=', 'True'), ('medium_id', '=', self.medium_id.id),
                                                  ('division_id', '=', self.division_id.id), ('standard_id', '=', self.standard_id.id)],limit=1)
        # self.class_teacher_id = record
        if self:
            self.write({'class_teacher_id': record})
        self.env['setu.teacher'].browse()

        # self.env['setu.student'].create({"name":"Hemangi"})

    #create method-----------
    # @api.model_create_multi
    # def create(self,vals_list):
    #     for vals in vals_list:
    #         record_id = self.env['setu.teacher'].search(
    #             [('is_teacher', '=', 'True'), ('medium_id', '=', vals.get('medium_id')),
    #              ('division_id', '=', vals.get('division_id')),
    #              ('standard_id', '=', vals.get('standard_id'))], limit=1)
    #         if record_id:
    #             vals.update({"class_teacher_id": record_id.id})
    #
    #         if not vals.get('name'):
    #             vals['middle_name'] = 'student'
    #
    #     res = super(SetuStudent, self).create(vals_list)
    #     # record = self.env['setu.teacher'].search([('is_teacher', '=', 'True'), ('medium_id', '=', res.medium_id.id),
    #     #                                           ('division_id', '=', res.division_id.id),
    #     #                                           ('standard_id', '=', res.standard_id.id)], limit=1)
    #     # if not res.class_teacher_id:
    #     #     res.class_teacher_id = record.id
    #
    #     return res


    #python constrains----------
    @api.constrains('roll_no')
    def check_duplicate_roll_no(self):
        for rec in self:
            existing_roll_no = self.search([('roll_no', '=', rec.roll_no), ('id', '!=', rec.id)])
            if existing_roll_no:
                raise ValidationError("Roll NO {} already exist".format(rec.roll_no))

    @api.constrains('first_name', 'last_name')
    def check_required(self):
        for name in self:
            if not(name.first_name and name.last_name):
                raise ValidationError("Please enter first name and last name...")


    # depends--------------------
    @api.depends('class_teacher_id')
    def _compute_teacher_email(self):
        for rec in self:
            if rec.class_teacher_id:
                rec.teacher_email = rec.class_teacher_id.email
            else:
                rec.teacher_email = False

    def _compute_teacher_phone(self):
        for rec in self:
            if rec.class_teacher_id:
                rec.teacher_phone = rec.class_teacher_id.phone
            else:
                rec.teacher_phone = False

    @api.depends()
    def _compute_is_above_18(self):
        today = date.today()
        for student in self:
            if student.date_of_birth:
                birthDate = student.date_of_birth
                age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
                student.is_above_18 = age > 18
            else:
                student.is_above_18 = False

    # @api.onchange('date_of_birth')
    # def _onchange_is_above_18(self):
    #     today = date.today()
    #     for student in self:
    #         if student.date_of_birth:
    #             birthDate = student.date_of_birth
    #             age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    #             student.is_above_18 = age > 18
    #         else:
    #             student.is_above_18 = False

    # @api.onchange('class_teacher_id')
    # def _onchange_teacher_phone(self):
    #     for rec in self:
    #         if rec.class_teacher_id:
    #             rec.teacher_phone = rec.class_teacher_id.phone
    #         else:
    #             rec.teacher_phone = False














