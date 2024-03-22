from  odoo import fields,models,api

class SetuGrade(models.Model):
    _name = "setu.grade"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name",tracking=True)
    result = fields.Boolean(string="Result")
    marks = fields.Integer(string="Marks")
    scorer = fields.Boolean(string="scorer")
    grade_line_ids = fields.One2many('setu.grade.line','grade_id', string="Grade Lines")

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('name_unique', 'unique(name)', "Name Must Be Unique."),
    ]


    @api.model
    def create(self, vals_list):
        if vals_list.get('marks') > 18:
            vals_list.update({'scorer': True})
        res = super(SetuGrade, self).create(vals_list)
        to_confirm = res.filtered(lambda wo: wo.name in ("Ki", "Li"))
        to_confirm._action_confirm()
        return res
    def _action_confirm(self):
        self.result = True

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

