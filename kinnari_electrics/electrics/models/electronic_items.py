from odoo import fields,models, api,_
from odoo.exceptions import ValidationError

class ElectronicItems(models.Model):
    _name = "electronic.items"
    _description = "Electronic Items"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name",tracking=True)
    code = fields.Integer(string="Unique Code",tracking=True)
    user_ids = fields.One2many('users', 'electronic_item_id', string="Users")
    Is_item = fields.Boolean(string="IS_item")
    price = fields.Integer(string="Price of Product")
    ava = fields.Boolean(string="Stock Available or not?")
    stock = fields.Integer(string="Stock of Product")
    updated = fields.Boolean(string="Updated data")
    production_date = fields.Date(string="Production Date")
    validity = fields.Date(string="Product Validity")


    def write(self, vals):
        vals.update({'updated': True})
        rec = super(ElectronicItems, self).write(vals)
        return rec



    def copy(self, default=None):
        default = dict(default or {})
        default['code'] = self.code + 1
        return super(ElectronicItems, self).copy(default=default)

    @api.onchange('production_date', 'validity')
    def _check_dates_(self):
        for rec in self:
            if rec.production_date and rec.validity and rec.validity < rec.production_date:
                raise ValidationError(_('The production validity cannot be earlier than the production date.', ))







