from odoo import fields, models


class SetuStudent(models.Model):
    _name = "setu.student"


    first_name = fields.Char(string="First Name")
    middle_name = fields.Char(string="Middle Name")
    last_name = fields.Char(string="Last Name")
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender")
    date_of_birth = fields.Date(string='DOB')
    blood_group = fields.Char(string="Blood Group")
    weight = fields.Float(string="Weight")
    height = fields.Float(string="Height")
    state = fields.Char(string="State")
    terminate_reason = fields.Char(string="Terminate Reason")
    active = fields.Boolean(string="Active")
    standard_id = fields.Many2one('setu.class',string="Class")
    division_id = fields.Many2one('setu.standard.division' , string="Division")
    medium_id = fields.Many2one('setu.standard.medium' , string="Medium")
    school_id = fields.Many2one('setu.school' , string="School")
    admission_date = fields.Date(string="Admission Date")
    academic_year_id = fields.Many2one('setu.academic.year',string="Year" )
    roll_no = fields.Integer(string="Roll")
    cast_id =  fields.Many2one('setu.student.cast',string="Cast")
    mother_tongue_id = fields.Many2one('setu.mother.tongue',string="Mother Tongue")
    teacher_id = fields.Many2one('setu.teacher',string="Class Teacher")

    def write(self, vals):
        if not vals.get('teacher_id'):
            record = self.env['setu.teacher'].search('|',
                [('city', 'ilike', 'rajkot'),
                 ('is_teacher', '=', True),
                 ('standard_id', '=', self.standard_id.id),
                 ('school_id','=',self.school_id.id),
                 ('division_id','=',self.division_id.id),
                 ('medium_id','=',self.medium_id.id)], limit=1)
            vals.update({'teacher_id': record.id})
        rec = super(SetuStudent, self).write(vals)
        return rec





    # def write(self, vals):
    #     record = self.env['teacher'].search(
    #         [('is_teacher', '=', True), ('standard_id', '=', self.standard_id.id)],limit=1)
    #     if record:
    #         vals.update({'teach_id': record.id})
    #     rec = super(SetuStudent, self).write(vals)
    #     return rec

    # record1 = self.env['setu.class'].search([('id','=','setu_teacher.standard_id')],limit=1)
        # print(record1)
    # rec = self.env['setu.teacher'].search([('standard_id', '=', self.standard_id.id)], limit=1)
    # self.teacher_id = rec.id

    # def write(selfself,vals):
    #     if vals.get('first_name'):
    #         rec = self.env['setu.teacher'].search('standard_id','=',self.standard_id)
    #         if rec:
    #             rec.write({'teacher_id':''})

    # @api.constrains('assignment_domain')
    # def _constrains_name(self):
    #     for record in self:
    #         try:
    #             domain = literal_eval(team.assignment_domain or '[]')
    #             if domain:
    #                 self.env['crm.lead'].search(domain, limit=1)
    #         except Exception:
    #             raise exceptions.ValidationError(
    #                 _('Assignment domain for team %(team)s is incorrectly formatted', team=team.name))

    # _sql_constraints = [
    #
    # ('not_active',
    #  'CHECK (active == False)',
    #  'Rule must have at least one checked access right!'),
    # ]
    # ('weight_data', 'CHECK(weight>0)', "Weight must grater than zero"),
    # ('height_data', 'CHECK(height>0)', "Height must grater than zero"),




