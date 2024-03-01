from odoo import models, fields

class State(models.Model):

    _name = "state"
    _description = "State"
    _rec_name = "name"

    state_id = fields.Char(string='State ID', required=True, copy='False')
    name = fields.Char(string = 'State', required = True)
    # city = fields.Char(string='City')
    # village = fields.Char(string='Village', required=True)
    # par_id = fields.One2many('partner', string="State")


