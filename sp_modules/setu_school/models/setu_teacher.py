from odoo import fields, models


class SetuTeacher(models.Model):
    _name = 'setu.teacher'
    _description = 'Teachers'

    name = fields.Char(string='Name')

    standard_id=fields.Many2one('setu.standard.standard',string='Standard',help='Responsibility of Academic Class')
    subject_ids=fields.Many2many('setu.subject',string='Subject ID')
    school_id=fields.Many2one('setu.school',string='School ID')
    student_ids=fields.One2many('setu.student','class_teacher_id',string='Student IDs')
    # class_ids=fields.One2many('setu.class','teacher_ids',string='Class IDs') #sdjfhksdjfhkjsdfhk
    class_teacher=fields.Boolean(string='Class Teacher')

    workphone = fields.Char(string='Work Phone', unaccent=False)
    workemail = fields.Char(string='Work Email')
    workaddress = fields.Text(string='Work Address')
    workcity = fields.Many2one('city',string='Work City')
    workstate = fields.Many2one('state',string='Work State')
    workcountry = fields.Many2one('country',string='Work Country')
    workzip = fields.Char(string='Work Zip')

    homephone = fields.Char(string='Home Phone', unaccent=False)
    homeemail = fields.Char(string='Home Email')
    homeaddress = fields.Text(string='Home Address')
    homecity = fields.Many2one('city',string='Home City')
    homestate = fields.Many2one('state',string='Home State')
    homecountry = fields.Many2one('country',string='Home Country')
    homezip = fields.Char(string='Home Zip')


    # _sql_constraints = [
    #     (
    #         "check_credit_debit",
    #         "CHECK(display_type IN ('line_section', 'line_note') OR credit * debit=0)",
    #         "Wrong credit or debit value in accounting entry !"
    #     ),

