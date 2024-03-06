from odoo import api,fields, models

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


    @api.model
    def create(self, vals_list):
        if not vals_list.get('phone'):
            vals_list.update({'phone':'985632147'})

        # vals_list.update({'gender': 'female'})
        res = super(Admisssion_form, self).create(vals_list)
        # res.gender = 'female'

        return res

