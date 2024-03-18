from odoo import api, models, fields
from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = "setu.student"
    _description = "Student"

    first_name = fields.Char(string='First Name')
    middle_name = fields.Char(string='Middle Name')
    last_name = fields.Char(string='Last Name')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    date_of_birth = fields.Date(string='DOB')
    blood_group = fields.Char(string='Blood Group')
    weight = fields.Integer(string='Weight')
    height = fields.Integer(string='Height')
    state = fields.Char(string='State')
    terminate_reason = fields.Char(string='Terminate Reason')
    active = fields.Boolean(string='Active')
    standard_id = fields.Many2one('setu.class', string='Class')
    division_id = fields.Many2one('setu.standard.division', string='Division')
    medium_id = fields.Many2one('setu.standard.medium', string='Medium')
    school_id = fields.Many2one('setu.school', string='School')
    admission_date = fields.Date(string='Admission Date')
    academic_year_id = fields.Many2one('setu.academic.year', string='Year')
    roll_no = fields.Integer(string='Roll No')
    cast_id = fields.Many2one('setu.student.cast', string='Cast')
    mother_toungue_id = fields.Many2one('setu.mother.toungue', string='Mothe Toungue')
    teacher_id = fields.Many2one('setu.teacher', string='Teacher')
    # class_teacher_id = fields.Many2one('setu.teacher', string='Teacher')

    @api.model
    def create(self, vals):
        if not vals.get('gender'):
            vals.update({'gender':'female'})
        rec = super(Student, self).create(vals)
        return rec

    def write(self, vals):
        if vals.get('last_name'):
            vals.update({'last_name':'Patel'})
        rec = super(Student, self).write(vals)
        return rec

    @api.model
    def unlink(self, vals):
        # self.first_name.unlink()
        for records in self:
            if records.first_name:
                raise ValidationError('can not be deleted.')
        return super(Student, self).unlink()

    # @api.model
    # def unlink(self):
        # for records in self:
        #     if records.:
        #         raise UserError(_('You cannot Delete this record'))
        # return super(PurchasePerformance, self).unlink()


    #
    # @api.model
    # def create(self, vals):
    #     if not vals.get('state'):
    #         vals.update({'state':'Gujarat'})
    #     sta = super(Student, self).create(vals)
    #     return sta
    #
    # @api.model
    # def create(self, vals):
    #     if not vals.get('active'):
    #         vals.update({'active':True})
    #     red = super(Student, self).create(vals)
    #     return red

    # @api.model
    # def create(self, vals):
    #     if not vals.get('terminate_reason'):
    #         vals.update({'terminate_reason':'higher study'})
    #     recs = super(Student, self).create(vals)
    #     return recs

    # def write(self, vals):
    #     recs= self.env['setu.teacher'].search([('active', '=', True)], limit=1)
    #     if recs:
    #         vals.update({'teacher_id':recs.id})
    #     res = super(Student, self).write(vals)
    #     return res