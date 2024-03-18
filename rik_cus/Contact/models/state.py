from odoo import fields, models

class State(models.Model):
    _name = "state"
    _description = "State"
    order = "name desc"

    name = fields.Char(string="state_name")
    direction = fields.Selection(selection=[("east", "EAST"), ("west", "WEST"), ("south", "SOUTH"), ("north", "NORTH")],string="In which side of country?", default="north")
    sid = fields.Integer(string="state_id")
    country_id = fields.Many2one("country",string="country")
    c_id = fields.One2many("customer", "state_id", string="customer")
    
    
    
