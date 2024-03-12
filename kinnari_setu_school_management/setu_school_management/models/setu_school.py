from odoo import fields, models,api

class SetuSchool(models.Model):
    _name = "setu.school"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    street = fields.Char(string="State")
    city = fields.Char(string="City")
    state_id = fields.Many2one('state', string="State Name")
    zip = fields.Integer(string="Zip")
    country_id = fields.Many2one('country', string="Country Name")
    required_age = fields.Integer(name="Minimum Age")
    school_standard_ids = fields.Many2many('setu.standard.standard' , string="Standards")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone" , help="Enter Mobile Number", size=10)

    @api.model
    def create(self, vals_list):
        if not vals_list.get('phone'):
            vals_list.update({'phone':'281'})
        res = super(SetuSchool,self).create(vals_list)
        return res

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('name_unique', 'unique(name)', "Name Must Be Unique."),
        ('phone_no_length', 'CHECK(LENGTH(phone) = 10)', "Phone must have 10 digit")
    ]

