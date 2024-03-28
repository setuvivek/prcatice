from odoo import fields, models,api, _
from odoo.exceptions import ValidationError

class SetuTeacher(models.Model):
    _name = "setu.teacher"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender",tracking=True)
    postgraduate = fields.Boolean(string="Have Master Degree?")
    master = fields.Selection(selection=[('maths','maths'),('physics','physics'),('chemistry','chemistry'),('biology','biology'),('other','other')],string="Master In")
    add = fields.Char(string="Write about it")
    sure = fields.Boolean(string="Are you want to add Personal details?")
    email = fields.Char(string="Email")
    mobile = fields.Char(string="mobile" , help="Enter mobile Number" , size=10)
    phone = fields.Char(string="Phone", help="Enter Phone Number" , size=10)
    standard_id = fields.Many2one('setu.class', string="Responsibility of Academic Class")
    division_id = fields.Many2one('setu.standard.division', string="Division")
    medium_id = fields.Many2one('setu.standard.medium', string="Medium")
    school_id = fields.Many2one('setu.school', string="Campus")
    subject_ids = fields.Many2many('setu.subject', 'setu_teachers_subjects', string="Subject")
    student_ids = fields.One2many('setu.student','teacher_id', string="Students")
    is_teacher = fields.Boolean(string="Is teacher")
    address = fields.Boolean(string="Are You want to add  Home Address?")
    city_id = fields.Many2one('city', string="City Name")
    state_id = fields.Many2one('state', string="State Name")
    country_id = fields.Many2one('country', string="Country Name")
    zip = fields.Char(string="zip")


    @api.model
    def create(self, vals_list):
        if not vals_list.get('phone'):
            vals_list.update({'phone': '281'})
        res = super(SetuTeacher, self).create(vals_list)
        return res


    _sql_constraints = [
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('name_unique', 'unique(name)', "Name Must Be Unique."),
    ]


    @api.constrains('zip')
    def _verify_zip(self):
        for rec in self:
            if rec.zip and not rec.zip.isdigit():
                raise ValidationError(_("The zip must be a sequence of digits."))






    # def write(self,vals):
    #     res = super(SetuTeacher).write(vals)
    #     if 'teacher_fall' in vals:
    #         teacher_fall = vals.get('is_teacher')
    #         if not teacher_fall:
    #             for rec in self:
    #                 rec.student_ids.write({'state':'rajkot'})
    #     return res

