from odoo import fields, models

class Location(models.Model):
    _name = "location"
    _description = "Location"
    _rec_name = "place_name"

    place_name = fields.Char(string="Name of place")
    schedule = fields.Datetime(string="Schedule")
    event_name = fields.Char(string="Name of event")
    Transportation = fields.Float(string="Transportation Fees")
    # attendee_id = fields.Many2one("attendee", string="attendee")
    attendee_ids = fields.One2many("attendee", "location_id", string="Other attendee")


