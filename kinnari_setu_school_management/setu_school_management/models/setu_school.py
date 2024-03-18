from odoo import fields, models,api

class SetuSchool(models.Model):
    _name = "setu.school"

    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    address = fields.Boolean(string="Are You want to add address?")
    city_id = fields.Many2one('city', string="City Name")
    state_id = fields.Many2one('state', string="State Name")
    country_id = fields.Many2one('country', string="Country Name")
    zip = fields.Integer(string="Zip")
    # required_age = fields.Integer(name="Minimum Age")
    school_standard_ids = fields.Many2many('setu.standard.standard' , string="Standards")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone" , help="Enter Mobile Number", size=10)
    cname= fields.Char(string="Class name")
    is_school = fields.Boolean(string="Is_school")

    @api.model
    def create(self, vals_list):
        if not vals_list.get('zip'):
            vals_list.update({'zip':360005})
        res = super(SetuSchool,self).create(vals_list)
        return res

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('email'):
                vals['email'] = 'abc@gmail.com'
                # vals_list.update({'address':'abc'})
        res = super(SetuSchool, self).create(vals_list)
        return res

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
        ('name_unique', 'unique(name)', "Name Must Be Unique."),
        ('phone_no_length', 'CHECK(LENGTH(phone) = 10)', "Phone must have 10 digit")
    ]

