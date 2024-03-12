from odoo import fields, models, api


class SetuAdmissionForm(models.Model):
    _name = "setu.admission.form"

    name = fields.Char(string="Name" )
    address = fields.Char(string="Address")
    city=fields.Char(string="City")
    state=fields.Char(string="State")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone")
    dob = fields.Date(string="Date of Birth")
    class_id = fields.Many2one('setu.class', string="class")

    @api.model
    def create(self, vals_list):
        if not vals_list.get('phone'):
            vals_list.update({'phone': '281'})
        res = super(SetuAdmissionForm, self).create(vals_list)
        return res


    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('name_unique', 'unique(name)', "Name Must Be Unique."),
        ('phone_length', 'CHECK(LENGTH(phone) = 10)', "Phone must have 10 digit")
    ]