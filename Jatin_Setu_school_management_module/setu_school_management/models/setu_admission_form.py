from odoo import api,fields, models
from odoo.exceptions import MissingError, ValidationError, AccessError
class Admisssion_form(models.Model):
    _name = "setu.admission.form"
    _description = "setu_admission_form"

    name = fields.Char(string="Student Name", required=True)
    class_id = fields.Many2one("setu.class",string='Class')
    address = fields.Char(string="Address")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    dob = fields.Date(string="DOB")
    state = fields.Char(string="State")
    # status = fields.Selection(selection=[("female", "Female"), ("male", "Male")])

    # def Object_butt(self):
    #     self.status = "male"
    #
    # def Object_buttt(self):
    #     self.status = "female"


    # @api.model
    # def create(self, vals_list):
    #     if not vals_list.get('phone'):
    #         vals_list.update({'phone':'98512345'})
    #
    #     # vals_list.update({'gender': 'female'})
    #     res = super(Admisssion_form, self).create(vals_list)
    #     res.address = 'Rajkot'
    #
    #     return res

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('phone'):
                vals.update({'phone': '98512345'})

        # vals_list.update({'gender': 'female'})
        res = super(Admisssion_form, self).create(vals_list)
        res.address = 'Rajkot'

        return res

    @api.constrains
    def unique_name(self):
        for db in self:
            if len(db.phone) < 4:
                raise ValidationError("Address length is less then 4")
