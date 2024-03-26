from odoo import fields, models , api , _
from odoo.exceptions import ValidationError


class SetuClass(models.Model):
    _name = "setu.class"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    is_teacher = fields.Boolean(string="Are You want to select teacher?")
    class_teacher_id1 = fields.Many2one('setu.teacher', string="Class Teacher")
    mobile = fields.Char(string="Teacher Mobile Number" , compute="_class_teacher_mobile" , store=True)
    email = fields.Char(string="Teacher Email" , compute="_class_teacher_mobile" , store=True)
    teacher_ids = fields.Many2many('setu.teacher', 'class_teacher', string="Teachers")
    is_stu = fields.Boolean(string="Are You want to select students?")
    student_ids = fields.Many2many('setu.student', 'class_student', string="Students")
    is_school = fields.Boolean(string="Are You want to choose school?")
    school_ids = fields.Many2many('setu.school', 'class_school', string="Schools")
    is_sub = fields.Boolean("Are you want to select subjects?")
    subject_ids = fields.One2many('setu.subject', 'standard_id', string="Subjects")

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Names must be unique'),
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('name_nospaces', "CHECK(name NOT LIKE '% %')","Name cannot contain spaces"),
    ]

    def write(self,vals):
        if vals.get('name'):
            vals.update({'name':'Patel'})
        rec = super(SetuClass, self).write(vals)
        return rec

    @api.depends('class_teacher_id1','mobile')
    def _class_teacher_mobile(self):
        for rec in self:
            if rec.class_teacher_id1:
                rec.mobile = rec.class_teacher_id1.mobile
                rec.email = rec.class_teacher_id1.email
            else:
                rec.mobile = False
                rec.email = False




























