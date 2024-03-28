from odoo import api,fields, models
from odoo.exceptions import MissingError, ValidationError, AccessError
class Admisssion_form(models.Model):
    _name = "setu.admission.form"
<<<<<<< HEAD
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name" )
    unique_id = fields.Integer(string="Unique Id")
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender")
    address = fields.Boolean(string="Are You want to add Address?")
    city_id = fields.Many2one('city', string="City Name")
    state_id = fields.Many2one('state', string="State Name")
    country_id = fields.Many2one('country', string="Country Name")

=======
    _description = "setu_admission_form"

    name = fields.Char(string="Student Name", required=True)
    class_id = fields.Many2one("setu.class",string='Class')
    address = fields.Char(string="Address")
>>>>>>> 0c53dcac5aa5f8ad5e4668828bd4bbe6b6c4ec57
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
    def action_but(self):
        self.phone = "12345"
    

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('phone'):
                vals.update({'phone': '98512345'})

        # vals_list.update({'gender': 'female'})
        res = super(Admisssion_form, self).create(vals_list)
        res.address = 'Rajkot'

        return res

<<<<<<< HEAD

    def copy(self,default=None):
        default = dict(default or {})
        default['unique_id'] = self.unique_id + 1
        return super(SetuAdmissionForm,self).copy(default=default)

    def default_get(self,fields):
        res = super(SetuAdmissionForm, self).default_get(fields)
        res.update({'phone': 91})
        return res









    # def reset_data(self,vals):
    #     if vals.get():
    #         vals.update({})
    #     self.env['setu.admission.form'].write(vals)

    # def write(self, vals):
    #     if vals.get('email'):
    #         vals['email'] = self.env['setu.admission.form']._clean_email(vals['email'])

    # def write(self,vals):
    #     if vals:
    #         vals.update({'name':'','address':'','city':'','state':''})
    #     rec = super(SetuAdmissionForm,self).write(vals)
    #     return rec



        # self.unlink()
        # self.name = ''
        # self.address = ''
        # self.city = ''
        # self.state = ''
        # self.email = ''
        # self.dob = ''
        # self.class_id = ''






















    # @api.constrains('date_start', 'date_stop')
    # def _constrains_dates_(self):
    #     for rec in self:
    #         if rec.date_start and rec.date_stop and rec.date_start > rec.date_stop:
    #             raise ValidationError(_('The stop date cannot be earlier than the start date. ',))



    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if 'code_prefix_start' in vals and not vals.get('code_prefix_end'):
    #             vals['code_prefix_end'] = vals['code_prefix_start']
    #     res_ids = super(AccountGroup, self).create(vals_list)
    #     res_ids._adapt_accounts_for_account_groups()
    #     res_ids._adapt_parent_account_group()
    #     return res_ids



    #
    # _sql_constraints = [
    #     # Partial constraint, complemented by unique index (see below). Still
    #     # useful to keep because it provides a proper error message when a
    #     # violation occurs, as it shares the same prefix as the unique index.
    #     ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
    #     ('name_unique', 'unique(name)', "Name Must Be Unique."),
    # ]
=======
    @api.constrains
    def unique_name(self):
        for db in self:
            if len(db.phone) < 4:
                raise ValidationError("Address length is less then 4")
>>>>>>> 0c53dcac5aa5f8ad5e4668828bd4bbe6b6c4ec57
