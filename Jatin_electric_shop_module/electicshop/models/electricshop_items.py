from odoo import fields, models, api

class ElectricshopItems(models.Model):
    _name = "electricshop.items"
    _description = "Electricshop Items"
    # _rec_name = "no_of_order"
    # _order = 'date desc'
    name = fields.Char(string='Item Name')
    price = fields.Integer(string='Price')

    def copy(self, default=None):
        default = dict(default or {})
        count = 1
        coun=str(count)

        if default.get('name', True):
            default['name'] = self.name + coun

        return super(ElectricshopItems, self).copy(default)


