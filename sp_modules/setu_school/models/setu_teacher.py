from odoo import fields, models


class SetuTeacher(models.Model):
    _name = 'setu.teacher'
    _description = 'Teachers'

    name = fields.Char(string='Name', require=True)
    address = fields.Text(string='Address')
    city = fields.Char(string='City')
    state = fields.Char(string='State')
    phone = fields.Char(string='Phone', unaccent=False)
    email = fields.Text(string='Email')
    mobile = fields.Char(string='Mobile', unaccent=False)
    school_id=fields.Many2one('setu.school',string='School ID')
    subject_id=fields.Many2one('setu.subject',string='Subject ID')
    student_ids=fields.One2many('setu.student','class_teacher_id',string='Student IDs')
    class_ids=fields.One2many('setu.class','teacher_ids',string='Class IDs') #sdjfhksdjfhkjsdfhk
