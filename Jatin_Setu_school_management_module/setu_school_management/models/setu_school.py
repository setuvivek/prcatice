from odoo import fields, models

class School(models.Model):
    _name = "setu.school"
    _description = "setu_school"

    name = fields.Char(string="School Name" , required=True)
    address = fields.Char(string="Address")
    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street2")
    city = fields.Char(string="City")
    phone = fields.Char(string="Phone")
    email = fields.Char(string="Email")


