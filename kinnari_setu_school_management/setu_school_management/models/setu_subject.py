from odoo import fields, models , api

class SetuSubject(models.Model):
    _name = "setu.subject"

    name = fields.Char(string="Name" )
    code = fields.Char(string="Code")
    maximum_marks = fields.Float(string="Maximum Marks")
    minimum_marks = fields.Float(string="Minimum Marks")
    weightage = fields.Float(string="Weightage" , compute="_abc",store=True)
    standard_id = fields.Many2one( 'setu.class' , string="Class")
    student_ids = fields.Many2many('setu.student','subject_student', string="Students")
    standard_ids = fields.Many2many('setu.standard.standard','setu_subject_standards',string="Standards")
    teacher_ids = fields.Many2many('setu.teacher','setu_subject_teachers',string="Teachers")

    @api.depends('maximum_marks', 'minimum_marks')
    def _abc(self):
        for record in self:
            record.weightage = (record.maximum_marks + record.minimum_marks )/2

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('name_unique', 'unique(name)', "Name Must Be Unique."),
    ]