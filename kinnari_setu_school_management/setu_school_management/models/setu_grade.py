<<<<<<< HEAD
from odoo import fields,models,api,_
from  odoo.exceptions import  ValidationError
=======
from odoo import fields, models
>>>>>>> 0c53dcac5aa5f8ad5e4668828bd4bbe6b6c4ec57

class Grade(models.Model):
    _name = "setu.grade"
<<<<<<< HEAD
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name",tracking=True)
    result = fields.Boolean(string="Result",compute="_dep",store=True)
    marks = fields.Integer(string="Marks")
    scorer = fields.Boolean(string="scorer")
    grade_line_ids = fields.One2many('setu.grade.line','grade_id', string="Grade Lines")

    @api.depends('marks','result')
    def _dep(self):
        if self.marks > 40:
            self.result = True

    @api.onchange('marks', 'scorer')
    def _onc(self):
        if self.marks > 25:
            self.scorer = True




    # _sql_constraints = [
    #     # Partial constraint, complemented by unique index (see below). Still
    #     # useful to keep because it provides a proper error message when a
    #     # violation occurs, as it shares the same prefix as the unique index.
    #     ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
    #     ('name_unique', 'unique(name)', "Name Must Be Unique."),
    # ]

    #
    # @api.model
    # def create(self, vals_list):
    #     if vals_list.get('marks') > 18:
    #         vals_list.update({'scorer': True})
    #     res = super(SetuGrade, self).create(vals_list)
    #     return res





    #     to_confirm = res.filtered(lambda wo: wo.name in ("Ki", "Li"))
    #     to_confirm._action_confirm()
    #     return res
    # def _action_confirm(self):
    #     self.result = True

    # def create(self, values_list):
    #     # notification field: if not set, set if mail comes from an existing mail.message
    #     for values in values_list:
    #         a = values.get('marks')
    #         if a > 18:
    #             if 'scorer' not in values:
    #                 values['scorer'] = True
    #     new_mails = super(SetuGrade, self).create(values_list)
    #     return new_mails

    # if 'scorer' not in values and values.get('marks'):

    # def create(self,vals):
    #     for rec in vals:
    #         if rec.['marks'] > 18:
    #             rec['scorer'] : True
    #
    #     rec = super(SetuGrade,self).create(vals)
    #     return rec

=======
    _description = "setu_grade"

    name = fields.Char(string="Name")
    grade_lines_ids = fields.One2many("setu.grade.line","grade_id",string="Grade Lines")
>>>>>>> 0c53dcac5aa5f8ad5e4668828bd4bbe6b6c4ec57
