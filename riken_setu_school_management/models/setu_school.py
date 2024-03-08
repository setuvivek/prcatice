from odoo import models, fields


class SetuSchool(models.Model):
    _name = "setu.school"
    _description ="SetuSchool"
    _rec_name = "name"

    name = fields.Char(string="Name")
    # city = fields.Char(string="City")
    state = fields.Char(string="State")
    phone = fields.Integer(string="Phone")
    email = fields.Char(string="Email")

