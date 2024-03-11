from odoo import fields, models

class School(models.Model):
    _name = "setu.school"
    _description = "setu_school"

    name = fields.Char(string="School Name" , required=True)
    code = fields.Char(string="Code")
    street = fields.Char(string="Address")
    city = fields.Char(string="City")
    state_id = fields.Many2one("state",string="State")
    zip = fields.Char(string="Zip")
    country_id = fields.Many2one("country", string="Country")
    required_age = fields.Integer(string="Minimum Age")
    school_standard_ids = fields.Many2many("setu.standard.standard",string="Standards")



