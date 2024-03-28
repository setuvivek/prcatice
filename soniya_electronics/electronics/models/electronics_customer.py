from odoo import api, models, fields

class ElectronicsCustomer(models.Model):
    _name = "electronics.customer"
    _description = "Customer"
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string = 'Name')
    phone = fields.Integer(string = 'Phone')
    email = fields.Char(string = 'Email')
    address = fields.Char(string = 'Address')
    pan_no = fields.Integer(string='PAN')
    paid = fields.Boolean(string='Fault')
    item_id = fields.Many2one('electronics.items', string='Select Item')
    fault = fields.Char(string='Problem')
    city_id = fields.Many2one('city', string='City')
    state_id = fields.Many2one(related='city_id.state_id', string='State')
    country_id = fields.Many2one(related='city_id.city_ids', string='Country')
    item_ids = fields.Many2many('electronics.items', string='Product Name')
    vendor_id = fields.Many2one('electronics.vendor', string='Vendor')
    total = fields.Float(string='Total', compute='_compute_total')


    _sql_constraints = [
        ('pan_uniq', 'unique (pan_no)', "PAN already exists!"),
        ('phone_uniq', 'unique(phone)', "User with this phone already exists!")
    ]

    @api.model
    def default_get(self, fields_list):
        default = super(ElectronicsCustomer, self).default_get(fields_list)
        default['email'] = 'e.g. someone@yahoo.com'
        return default

    @api.depends('item_ids')
    def _compute_total(self):
        for recs in self:
             recs.total = sum(recs.item_ids.mapped('price')) if recs.item_ids else 0











