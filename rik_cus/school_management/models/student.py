from odoo import models, fields, api

class Student(models.Model):
    _name = 'student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True, help="validation")
    std = fields.Integer(string='Std')
    cls = fields.Selection(selection=[('a','A'),('b','B')],string='Cls')
    gender = fields.Selection(selection=[('male','MALE'),('female','FEMALE'),('other','OTHER')],string='Gender', default="male")
    other = fields.Char(string="Other")
    age = fields.Integer(string='Age')
    birth_date = fields.Date(string="birth_date")
    teacher_id = fields.Many2one("teacher", string="Teacher")
    teacher_ids = fields.Many2many("teacher", "science_teacher", "student", "teacher", string="science_teacher")
    math_teacher_ids = fields.Many2many("teacher", "math_teacher", "student", "teacher", string="math_teacher")
    city_id = fields.Many2one("city", string="City")



    def write(self, vals):
        rec = self.env['teacher'].search([('city_id', '=', 'rajkot')], limit=1)
        if rec:
            vals.update({'teacher_id': rec.id})
        res = super(Student, self).write(vals)
        return res

