from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class Users(models.Model):
    _name = "users"
    _description = "User"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name",tracking=True)
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], default="male", string="Gender")
    phone = fields.Char(string="Phone", help="Enter Phone Number", size=10)
    email = fields.Char(string="Email")
    date_of_birth = fields.Date(string='DOB')
    code = fields.Integer(string="Unique Code")
    address = fields.Boolean(string="Are You want to add Resident Data?")
    personal_info = fields.Boolean(string="Are you want to add personal Information?")
    country_id = fields.Many2one('country', string="Country Name")
    state_id = fields.Many2one('state', string="State Name")
    city_id = fields.Many2one('city', string="City Name")
    zip = fields.Integer(string="zip", related='city_id.zip')
    electronic_item_id = fields.Many2one('electronic.items', string="Electric Item")
    codee = fields.Integer(string="Code Of Electronic Item", compute="_depends_code", store=True)
    price = fields.Integer(string="Price of Product", related='electronic_item_id.price')
    stock = fields.Integer(string="Stock of Product", related='electronic_item_id.stock')
    production_date = fields.Date(string="Production Date", related='electronic_item_id.production_date')
    validity = fields.Date(string="Product Validity", related='electronic_item_id.validity')
    quan = fields.Integer(string="Quantity")
    total = fields.Integer(string="Amount", compute="_depends_amount", store=True)
    offer = fields.Boolean(string="You are eligible for offer", compute="_depends_offer", store=True)
    after = fields.Integer(string="Total Amount after getting offer", compute="_depends_after", store=True)
    purchase = fields.Boolean(string="Are You want to Purchase?")
    msg = fields.Char(string="msg" , readonly=True)
    feedback = fields.Boolean(string="Are you want to give feedback?")

    def purchased(self):
        self.msg = "Thanks For Purchase!!!!!!"


    @api.depends('offer', 'total')
    def _depends_offer(self):
        for rec in self:
            if rec.total > 999:
                rec.offer = True

    @api.depends('total', 'after')
    def _depends_after(self):
        for rec in self:
            if rec.total:
                a = rec.total * 0.1
                rec.after = rec.total - a



    @api.depends('electronic_item_id', 'codee')
    def _depends_code(self):
        for rec in self:
            if rec.electronic_item_id:
                rec.codee = rec.electronic_item_id.code
            else:
                rec.codee = False

    @api.depends('price', 'quan', 'total')
    def _depends_amount(self):
        for rec in self:
            rec.total = rec.price * rec.quan

    @api.onchange('stock', 'quan')
    def onchange_check_dates(self):
        for rec in self:
            if rec.stock and rec.quan and rec.quan > rec.stock:
                raise ValidationError(_('Stock Not Available', ))


    def copy(self, default=None):
        default = dict(default or {})
        default['code'] = self.code + 1
        return super(Users, self).copy(default=default)

# def default_get(self,fields):
#     res = super(Users, self).default_get(fields)
#     if {'citizenship':'Indian'}:
#         res.update({'phone': 91})
#     return res
# @api.model
# def create(self, vals):
#     if not vals.get('zip'):
#         if vals.get('city_id'):
#             if vals['city_id'] == 1:
#                 vals.update({'zip':360005})
#     rec = super(Users, self).create(vals)
#     return rec

# def default_get(self, fields):
#     res = super(Users, self).default_get(fields)
#     record = self.env['country'].search([('phone_code','!=',None)])
#     if record:
#         res.update({'phone': record.phone_code})
#     return res
