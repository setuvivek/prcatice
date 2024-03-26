from odoo import fields,models,api

class SetuGradeLine(models.Model):
    _name = "setu.grade.line"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    from_mark = fields.Date(string="From Mark")
    to_mark = fields.Date(string="To Mark")
    name = fields.Char(string="Name",tracking=True)
    fail = fields.Boolean(string="Fail")
    grade_id = fields.Many2one('setu.grade' , string="Grade")
    names = fields.Char(string="Grade Name", tracking=True)
    result = fields.Boolean(string="Grade Result")
    # marks = fields.Integer(string="Grade Marks" )
    # scorer = fields.Boolean(string="Grade scorer", compute="_oncha" , store=True)

    # _sql_constraints = [
    #     # Partial constraint, complemented by unique index (see below). Still
    #     # useful to keep because it provides a proper error message when a
    #     # violation occurs, as it shares the same prefix as the unique index.
    #     ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
    #     ('name_unique', 'unique(name)', "Name Must Be Unique."),
    # ]

    @api.onchange('grade_id','names','result','marks','scorer')
    def _oncha(self):
        for rec in self:
            if rec.grade_id:
                rec.names = rec.grade_id.name
                rec.result = rec.grade_id.result
                # rec.marks = rec.grade_id.marks
                # rec.scorer = rec.grade_id.scorer


                # obj = self.env['setu.grade'].browse([self.id])
                # obj.marks
                # obj.scorer





    # def browse(self,id):
    #     return self.env['setu.grade'].browse([id])


