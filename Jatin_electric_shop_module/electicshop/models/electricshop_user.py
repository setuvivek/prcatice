from odoo import fields, models, api

class ElectricshopUser(models.Model):
    _name = "electricshop.user"
    _description = "Electricshop User"
    # _rec_name = "no_of_order"
    # _order = 'date desc'
    name = fields.Char(string='Name')
    mobile_no = fields.Char(string="Mobile NO.")
    address = fields.Char(string="address")
    items_id = fields.Many2one('electricshop.items', string='Items')
    bill_id = fields.Many2one('electricshop.bill', string='Bill User')
