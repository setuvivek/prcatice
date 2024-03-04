from odoo import fields, models

class Attendee(models.Model):
    _name = "attendee"
    _description = "Attendee"

    name = fields.Char(string="Name", required=True)
    mail = fields.Char(string="Email", copy=False)
    is_age = fields.Boolean(string="Is Age Above 10?", required=True)
    gender = fields.Selection(selection=[("male","MALE"),("female","FEMALE")], string="Gender")
    phn = fields.Integer(string="Phone number" , defalult="0000000000000", help="provide current phone number")
    birthdate = fields.Date(string="BirthDate")
    location_id = fields.Many2one("location", string="Location")
    # loc_ids = fields.One2many("location", "attendee_id",  string="Location")
    location_ids = fields.Many2many("location", string="OTHER LOCATION")

