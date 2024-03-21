from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SetuTeacher(models.Model):
    _name = "setu.teacher"
    _description = "SetuTeacher"
    _rec_name = "name"
    _inherit = ['mail.thread','mail.activity.mixin']

    standard_id = fields.Many2one("setu.standard.standard", string="Responsibility of Academic Class", tracking=True)
    subject_ids = fields.Many2many("setu.subject", string="Subjects")
    school_id = fields.Many2one("setu.school", string="Campus", tracking=True)
    student_ids = fields.One2many("setu.student", "class_teacher_id", string="Student")
    name = fields.Char(string="Name", tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    phone = fields.Integer(string="Phone", tracking=True)
    email = fields.Char(string="Email", tracking=True)
    mobile = fields.Integer(string="Mobile", tracking=True)
    work_city_id = fields.Many2one("city", string="Work City", tracking=True)
    work_state_id = fields.Many2one("state", string="Work State", tracking=True)
    work_country_id = fields.Many2one("country", string="Work Country", tracking=True)
    home_city_id = fields.Many2one("city", string="Home City", tracking=True)
    home_state_id = fields.Many2one("state", string="Home State", tracking=True)
    home_country_id = fields.Many2one("country", string="Home Country", tracking=True)
    medium_id = fields.Many2one('setu.standard.medium', string="Medium", tracking=True)
    division_id = fields.Many2one('setu.standard.division', string="Division", tracking=True)
    class_teacher = fields.Boolean(string="Class Teacher", tracking=True    )

    @api.constrains('name')
    def _check_unique_teacher_name(self):
        for record in self:
            existing_teacher = self.env['setu.teacher'].search([('name', 'ilike', record.name)])
            if len(existing_teacher) > 1 or (len(existing_teacher) == 1 and existing_teacher[0] != record):
                raise ValidationError(f'Teacher name "{record.name}" already exists!')

                # raise ValidationError('Teacher name "{record.name}" already exists!')

    # _sql_constraints = [('teacher_name_unique', 'unique(name)', 'Teacher name already exists')]




    #
    # def update(self):
    #     rec = self.env['student'].search([('standard', '=', 4)], limit=1)
    #     if rec:
    #         rec.write({'teacher_id': rec.id})



