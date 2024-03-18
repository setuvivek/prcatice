from odoo import models, fields, api

class Teacher(models.Model):

    _name = "teacher"
    _description = "Teacher"
    _rec_name = "name"
    _order = "age desc"

    name = fields.Char(string='Name')
    gender = fields.Selection(selection=[('male', 'MALE'), ('female', 'FEMALE')], string='Gender',default="male")
    age = fields.Integer(string='Age')
    phn_no = fields.Integer(string='Phn_No')
    city_id = fields.Many2one("city", string='City')
    joining_date = fields.Datetime(string="joining_date")
    student_ids = fields.One2many("student", "teacher_id", string="Student")
    department_ids = fields.One2many("department", "teacher_id", string="department")


    #department_id = fields.Many2one("department", string="department")

    #
    # @api.model_create_multi
    # def create(self, vals):
    #     if not vals.get('phn_no'):
    #         vals.update({'phn_no':'1111'})
    #     res = super('teacher',self).create(vals)
    #
    #     res.phn_no="2626"
    #     vals.update({'phn_no':'2121'})
    #     return res