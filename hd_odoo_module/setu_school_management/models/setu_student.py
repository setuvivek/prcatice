# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import AccessError, MissingError, ValidationError, UserError



class SetuStudent(models.Model):
    _name = 'setu.student'
    _description = 'Setu Student'

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

    # Integer-------------
    roll_no = fields.Integer(string='Roll No')
    weight = fields.Integer(string='Weight')
    height = fields.Integer(string='Height')

    # Boolean------------
    active = fields.Boolean(string='Active')

    # Selection-----------
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')])

    # Date----------------
    date_of_birth = fields.Date(string='DOB')

    # Datetime------------
    admission_date = fields.Datetime(string='Admission Date')

    # m2o-----------------
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')
    class_teacher_id = fields.Many2one('setu.teacher', string='Class Teacher')
    school_id = fields.Many2one('setu.school', string='School')
    standard_id = fields.Many2one('setu.class', string='Class')
    division_id = fields.Many2one('setu.standard.division', string='Division')
    medium_id = fields.Many2one('setu.standard.medium', string='Medium')
    academic_year_id = fields.Many2one('setu.academic.year', string='Year')
    mother_tongue_id = fields.Many2one('setu.mother.tongue', string='Mother Tongue')

    # m2m------------------
    teacher_ids = fields.Many2many('setu.teacher', 'student_teacher', 'student', 'teacher', string='Teacher')
    subject_ids = fields.Many2many('setu.subject', 'student_subject', 'student', 'subject', string='Subject')

    def action_done(self):
        record = self.env['setu.teacher'].search([('is_teacher', '=', 'True'), ('medium_id', '=', self.medium_id.id),
                                                  ('division_id', '=', self.division_id.id), ('standard_id', '=', self.standard_id.id)],limit=1)
        # self.class_teacher_id = record
        if self:
            self.write({'class_teacher_id': record})

        # self.env['setu.student'].create({"name":"Hemangi"})


    @api.model_create_multi
    def create(self,vals_list):
        for vals in vals_list:
            record_id = self.env['setu.teacher'].search(
                [('is_teacher', '=', 'True'), ('medium_id', '=', vals.get('medium_id')),
                 ('division_id', '=', vals.get('division_id')),
                 ('standard_id', '=', vals.get('standard_id'))], limit=1)
            if record_id:
                vals.update({"class_teacher_id": record_id.id})

        res = super(SetuStudent, self).create(vals_list)
        # record = self.env['setu.teacher'].search([('is_teacher', '=', 'True'), ('medium_id', '=', res.medium_id.id),
        #                                           ('division_id', '=', res.division_id.id),
        #                                           ('standard_id', '=', res.standard_id.id)], limit=1)
        # if not res.class_teacher_id:
        #     res.class_teacher_id = record.id
        # return res

    @api.constrains('roll_no')
    def check_duplicate_roll_no(self):
        for rec in self:
            existing_roll_no = self.search([('roll_no', '=', rec.roll_no), ('id', '!=', rec.id)])
            if existing_roll_no:
                raise ValidationError("Roll NO {} already exist".format(rec.roll_no))


