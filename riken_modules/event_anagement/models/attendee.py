from odoo import fields, models, api

class Attendee(models.Model):
    _name = "attendee"
    _description = "Attendee"

    name = fields.Char(string="Name", required=True)
    mail = fields.Char(string="Email", copy=False)
    is_age = fields.Boolean(string="Is Age Above 10?", required=True)
    gender = fields.Selection(selection=[("male","MALE"),("female","FEMALE")], string="Gender")
    phn = fields.Integer(string="Phone number" , defalult="0000000000000", help="provide current phone number")
    birthdate = fields.Date(string="BirthDate")
    location_id = fields.Many2one("location", string="Location")
    # loc_ids = fields.One2many("location", "attendee_id",  string="Location")
    location_ids = fields.Many2many("location", string="OTHER LOCATION")
    student_id= fields.Many2one("student", string="Student")

    # @api.model_create_multi
    # def create(self, vals_list):
    #     if not vals_list.get('phn'):
    #         vals_list.update({'phn': '1111'})
    #     #vals.update({'phn': '2121'})
    #     res = super(Attendee, self).create(vals_list)
    #
    #     res.phn = "2626"
    #
    #     return res

