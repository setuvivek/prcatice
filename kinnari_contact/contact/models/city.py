from odoo import fields, models

class City(models.Model):
    _name = "city"
    _description = "City"

    name = fields.Char(string="Name",required=True)
    type = fields.Selection(selection=[('local','Local'),('medium','Medium'),('model','Model')],string="Public Life")
    smartcity = fields.Boolean(string="Smartcity", default=False)
    state_id = fields.Many2one('state',string="State")
    customer_ids = fields.One2many('contact.partner','city_id', string="Customer")



