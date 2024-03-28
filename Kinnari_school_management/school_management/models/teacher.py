from odoo import fields, models,api

class Teacher(models.Model):
    _name = "teacher"
    _description = "Teacher"
    _order = "result"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _inherit = ['mail_thread', 'mail_activity_mixin']

    name = fields.Char(string="Name")
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender")
    age = fields.Integer(string="age" , tracking=True)
    mobile = fields.Char(string="Mobileno", help="Enter Mobile Number", size=10)
    postgraduate = fields.Boolean(string="Postgraduate")
    result = fields.Float(string="Result", help="Enter result of Postgraduate")
    dob = fields.Date(string="Date of Birth")
    student_id = fields.One2many('student','teach_id1',string="Students")
    address = fields.Boolean(string="You want to add Resident Location")
    country_id = fields.Many2one('country', string="Country Name")
    state_id = fields.Many2one('state', string="State Name")
    city_id = fields.Many2one('city', string="City Name")
    priority = fields.Selection([('clear', 'Clear'), ('urgent', 'Urgent'),('normal', 'Normal'),('lower', 'Lower'),('high', 'High')])
    city = fields.Char(string="city")

    @api.model
    def create(self, vals_list):
        if not vals_list.get('priority'):
            vals_list.update({'priority':'normal'})

        res = super(Teacher,self).create(vals_list)
        return res

    _sql_constraints = [('mobile_length', 'CHECK(LENGTH(mobile) = 10)', "Mobile must have 10 digit"),
                        ('name_compulsory' , 'CHECK(name IS NOT NULL)','name should required'),]

    def create_data(self):
        self.priority = 'high'






        # if 'mobile' not in default_fields:
        #     default_fields.
        # #     return super().default_get(default_fields)
        # # default_name = self._context.get('default_name')
        # # default_code = self._context.get('default_code')
        # # if default_name and not default_code:
        # #     try:
        # #         default_code = int(default_name)
        # #     except ValueError:
        # #         pass
        # #     if default_code:
        # #         default_name = False
        # # contextual_self = self.with_context(default_name=default_name, default_code=default_code)
        # return super(AccountAccount, contextual_self).default_get(default_fields)

            # def _check_name(self, mobile, context=None):
    #     for val in self.read(mobile, ['mobile'], context=context):
    #         if val['mobile']:
    #             if len(val['mobile']) < 10:
    #                 return False
    #     return True
    #
    # _sql_constraints = [
    #     (_check_name, 'Mobile must have at least 10 digit', ['mobile'])
    # ]

    # def create_new_data(self, valuees):
    #     if valuees.get('name') == ('kinu'):
    #         self.student_id = self.env['student'].create({'name': 'lp', 'create_date': 'dob'})
    #     else:
    #         valuees['name'] = 'k'
    #     return super(Teacher, self).create(valuees)
    # @api.constrains('identification_id')
    # def check_identification_id(self):
    #     for rec in self:
    #         if len(rec.identification_id) != 11:
    #             raise ValidationError(_('Must be 11 Characters'))

       





















        # vals = [{'name': 'test 1'}]
        # self.env['model.teacher'].create(vals)
        # @api.model
        # def create(self, vals):
        # res1 = super(Teacher, self).create(vals_list)
        # for i in range(vals_list["result"]):
        #     super( self.env['result']).create({
        #         'result' : 50.00
        #         # 'model_id': res.id,
        #         # 'car_ref': "%s_%s" % (res.ref, i + 1),
        #         # 'name': "%s #%s" % (res.name, i + 1)
        #     })
        # return res1

        #
        # def create(self, vals):
        #     if vals.get('reference_no', _('New')) == _('New'):
        # vals_list['result'] = self.env['50']
        #     # 'hospital.patient') or _('New')
        # res1 = super(Teacher, self).create(vals_list)
        # return res1,res


    #
    #     self.create_otherModule_data()
    #     res1 = super(Teacher, self).create(vals_list)
    #     return res1
    #
    # def create_otherModule_data(self):
    #     line_dic = {
    #         'result':'50.00',
    #         # 'complete_name': self.complete_name,
    #         # 'code': code,
    #         # 'active': True,
    #     }
    #     self.env['module.teacher'].create(line_dic)




    # def reload_page(self):
    #     return self.env['teacher'].create({
    #                     'result': '33.3'
    #                 })

    #
    # def create_data(self):
    #     self.priority='high'


