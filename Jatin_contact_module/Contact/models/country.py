from odoo import fields, models

class Country(models.Model):
    _name = "country"
    _description = "country"

    name = fields.Char(string="Country Name",required=True)
    state = fields.Integer(string="No. Of State")
    secular = fields.Boolean(string="Secular")
    city_country_o2m_ids= fields.One2many("state","scountry_id",string="Add New  State")#//ama state  add kare che
    select_state_m2m_ids = fields.Many2many("city",string="Select State")
    city2_country_o2m_ids= fields.One2many("city","country_id",string="Add New Cityy")#ama city add kare
