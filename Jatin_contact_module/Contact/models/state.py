from odoo import fields, models

class State(models.Model):
    _name = "state"
    _description = "state"

    name = fields.Char(string="State Name",required=True)
    city = fields.Integer(string="No. Of City")
    scountry_id = fields.Many2one("country",string="Country Of State")
    city_o2m_ids = fields.One2many("city","state_id",string="Add New City")
    select_city_m2m_ids = fields.Many2many("city",string="Select City")
