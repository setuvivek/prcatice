from odoo import fields,models, api

class ElectronicItems(models.Model):
    _name = "electronic.items"
    _description = "Electronic Items"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Name")
    code = fields.Integer(string="Unique Code")
    user_ids = fields.One2many('users', 'electronic_item_id', string="Users")
    Is_item = fields.Boolean(string="IS_item")
    quality = fields.Selection(selection=[('best','best'),('medium','medium'),('low','low')], string="Quality")
    price = fields.Integer(string="Price of Product")
    ava = fields.Boolean(string="Stock Available or not?")
    stock = fields.Integer(string="Stock of Product")
    updated = fields.Boolean(string="Updated data")

    def write(self, vals):
        vals.update({'updated': True})
        rec = super(ElectronicItems, self).write(vals)
        return rec


    def copy(self, default=None):
        default = dict(default or {})
        default['code'] = self.code + 1
        return super(ElectronicItems, self).copy(default=default)






