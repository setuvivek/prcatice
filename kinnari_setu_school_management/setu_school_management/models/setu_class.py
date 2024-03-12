from odoo import fields, models , api , _
from odoo.exceptions import ValidationError


class SetuClass(models.Model):
    _name = "setu.class"

    name = fields.Char(string="Name")
    class_teacher_id1 = fields.Many2one('setu.teacher', string="Class Teacher")
    teacher_ids = fields.Many2many('setu.teacher', 'class_teacher', string="Teachers")
    student_ids = fields.Many2many('setu.student', 'class_student', string="Students")
    school_ids = fields.Many2many('setu.school', 'class_school', string="Schools")
    subject_ids = fields.One2many('setu.subject', 'standard_id', string="Subjects")

    _sql_constraints = [
        ('name_unique', 'unique(name)', 'Names must be unique'),
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ("uniq", "UNIQUE(class_teacher_id1)", "Models inherits from another only once"),
        ('name_nospaces', "CHECK(name NOT LIKE '% %')","Name cannot contain spaces"),
    ]

    def write(self,vals):
        if vals.get('name'):
            vals.update({'name':'Patel'})
        rec = super(SetuClass, self).write(vals)
        return rec














