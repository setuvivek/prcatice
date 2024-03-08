from odoo import api, models, fields

class Admission(models.Model):

    _name = "setu.admission"
    _description = "Setu_Admission"

    student_name = fields.Char(string='Name')
    class_id = fields.Many2one('setu.school', string='School')
    address = fields.Char(string='Address')

    email = fields.Char(string='email')
    phone = fields.Char(string='Phone')
    dob = fields.Date(string='Date')
    state = fields.Selection(selection=[('gujarat', 'Gujarat'), ('madhypradesh', 'MP'), ('bihar', 'Bihar'), ('punjab','Punjab'), ('rajasthan', 'Rajsthan')], string='State')
    # class_id = fields.Many2one('setu.school', string='School')

    status = fields.Selection(selection=[('draft', 'Draft'), ('done', 'Done')])

    def action_done(self):
        self.status = 'done'

    def action_draft(self):
        self.status = 'draft'


    # @api.model
    # def create(self, vals_list):
    #     if not vals_list.get('name'):
    #         vals_list.update({'name': 'abc'})
    #
    #     res = super(Admission, self).create(vals_list)
    #     return res




