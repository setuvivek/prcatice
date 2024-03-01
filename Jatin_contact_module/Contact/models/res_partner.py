from odoo import fields, models

class Res_partner(models.Model):
    _name = "setu.partner"
    _description = "Res_partner"

    name = fields.Char(string="Partner Name" , required=True)
    part_is_cust = fields.Boolean(string="Partner Is Customer?")
    city_m2o_id = fields.Many2one("city", string="Select City")