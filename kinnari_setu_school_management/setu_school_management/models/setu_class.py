from odoo import fields, models


class SetuClass(models.Model):
    _name = "setu.class"

    name = fields.Char(string="Name")
    class_teacher_id1 = fields.Many2one('setu.teacher', string="Class Teacher")
    teacher_ids = fields.Many2many('setu.teacher', 'class_teacher', string="Teachers")
    student_ids = fields.Many2many('setu.student', 'class_student', string="Students")
    school_ids = fields.Many2many('setu.school', 'class_school', string="Schools")
    subject_ids = fields.One2many('setu.subject', 'standard_id', string="Subjects")

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_unique', 'unique(name)', 'Names must be unique'),
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ("uniq", "UNIQUE(class_teacher_id1)", "Models inherits from another only once"),
        ('name_nospaces', "CHECK(name NOT LIKE '% %')","Name cannot contain spaces"),

        # ('size_gt_zero', 'CHECK (size>=0)', 'Size of the field cannot be negative.')
    ]












