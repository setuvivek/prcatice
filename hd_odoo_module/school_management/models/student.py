# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Student(models.Model):
    _name = 'student'
    _description = 'Student'
    # _rec_name = 'code'
    _order = 'id desc'

    #Char------------------
    name = fields.Char(string='Name', help='Student Name')
    sport = fields.Char(string='Sport')
    rank1 = fields.Char(string='Percentage')
    teacher_phone = fields.Char(string='Teacher Phone', _compute='_compute_teacher_phone')


    #Integer---------------
    roll_no = fields.Integer(string='Roll No', copy=False, help='Student Roll No')

    #Selection--------------
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    sem = fields.Selection(
        selection=[('even', 'Even'), ('odd', 'Odd')],
        string='Semester')
    even = fields.Selection(selection=[('2','2'), ('4','4'), ('6','6'), ('8','8')])
    odd = fields.Selection(selection=[('1','1'), ('3','3'), ('5','5'), ('7','7')])
    rank = fields.Selection(selection=[('rank1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')])
    status = fields.Selection(selection=[('draft', 'Draft'), ('confirm', 'Confirm'), ('cancel','Cancel')])

    #Boolean----------------
    is_present = fields.Boolean(string='Present')
    is_sport_person = fields.Boolean(string='Sport Person')
    is_topper = fields.Boolean(string='Topper')
    in_top_10 = fields.Boolean(string='In Top10')
    show_notebook = fields.Boolean(string='Show OOP Teacher')

    #Date-------------------
    student_dob = fields.Date(string="Date of Birth", help='Student Birth Date')

    #M2o--------------------
    teacher_id = fields.Many2one('teacher', string='Class Teacher', help='Many2one relation')
    course_id = fields.Many2one('course', string='Course', help='Many2one relation')
    dept_id = fields.Many2one('department', string='Department', help='Many2one relation')

    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')


    #M2m----------------------
    teacher_ids = fields.Many2many('teacher', string='DS Teacher', help='Many2many relation')
    dbms_teacher_ids = fields.Many2many('teacher', 'ds_teacher', 'student', 'teacher', string='DBMS Teacher',
                                        help='Many2many relation')
    oop_teacher = fields.Many2many('teacher', 'oop_teacher', 'student', 'teacher', string='OOP Teacher',
                                   help='Many2many relation')

    #Create with single record--------------------
    # @api.model
    # def create(self, vals):
    #     if not vals.get('roll_no'):
    #         vals.update({'roll_no': '1'})
    #     res = super(Student, self).create(vals)
    #     return res

    #create with multiple record-------------------
    @api.model_create_multi
    def create(self, vals_list):

        for vals in vals_list:
            if not vals.get('roll_no'):
                vals['roll_no'] = '2'

        # for vals in vals_list:
        #     record_id = self.env['teacher'].search(
        #         [('dept_id', '=', vals.get('dept_id')), ('course_id', '=', vals.get('course_id'))], limit=1)
        #     if record_id:
        #         vals.update({"teacher_id": record_id.id})

        res = super(Student, self).create(vals_list)

        # if not res.roll_no:
        #     res.roll_no = 3

        # record = self.env['teacher'].search([('dept_id', '=', res.dept_id.id), ('course_id', '=', res.course_id.id)], limit=1)
        # if not res.teacher_id:
        #     res.teacher_id = record.id

        return res





























    # def create(self, vals_list):
    #     vals_list = [{}]
    #     return super(Student, self).create(vals_list)






