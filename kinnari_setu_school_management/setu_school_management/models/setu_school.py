from odoo import fields, models

class School(models.Model):
    _name = "setu.school"
<<<<<<< HEAD
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name",tracking=True)
    code = fields.Char(string="Code",tracking=True)
    address = fields.Boolean(string="Are You want to add address?")
    city_id = fields.Many2one('city', string="City Name")
    state_id = fields.Many2one('state', string="State Name")
    country_id = fields.Many2one('country', string="Country Name")
    zip = fields.Integer(string="Zip")
    # required_age = fields.Integer(name="Minimum Age")
    school_standard_ids = fields.Many2many('setu.standard.standard' , string="Standards")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Phone" , help="Enter Mobile Number", size=10,tracking=True)
    cname= fields.Char(string="Class name")
    is_school = fields.Boolean(string="Is_school", compute ="_abc", store=True)

    @api.depends('cname','is_school')
    def _abc(self):
        if self.cname:
            self.is_school = True


    #
    #
    # def _abc(self,vals):
    #     for rec in vals:
    #         if rec.cname=="abc":
    #             rec.update({'is_school': True})

        # if self.cname == "abc":
        #     self.is_school = True
        #
=======
    _description = "setu_school"

    name = fields.Char(string="School Name" , required=True)
    code = fields.Char(string="Code")
    street = fields.Char(string="Address")
    city = fields.Char(string="City")
    state_id = fields.Many2one("state",string="State")
    zip = fields.Char(string="Zip")
    country_id = fields.Many2one("country", string="Country")
    required_age = fields.Integer(string="Minimum Age")
    school_standard_ids = fields.Many2many("setu.standard.standard",string="Standards")
>>>>>>> 0c53dcac5aa5f8ad5e4668828bd4bbe6b6c4ec57


<<<<<<< HEAD
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('email'):
                vals['email'] = 'abc@gmail.com'
                # vals_list.update({'address':'abc'})
        res = super(SetuSchool, self).create(vals_list)
        return res

    # _sql_constraints = [
    #     # Partial constraint, complemented by unique index (see below). Still
    #     # useful to keep because it provides a proper error message when a
    #     # violation occurs, as it shares the same prefix as the unique index.
    #     ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
    #     ('name_unique', 'unique(name)', "Name Must Be Unique."),
    #     ('phone_no_length', 'CHECK(LENGTH(phone) = 10)', "Phone must have 10 digit")
    # ]

    def default_get(self,fields):
        rec = super(SetuSchool,self).default_get(fields)
        rec.update({'code':1})
        return rec


=======
>>>>>>> 0c53dcac5aa5f8ad5e4668828bd4bbe6b6c4ec57

