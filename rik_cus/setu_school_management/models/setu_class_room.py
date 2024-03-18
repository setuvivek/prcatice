from odoo import models, fields

class SetuClassRoom(models.Model):
    _name = "setu.class.room"
    _description = "SetuClassRoom"

    name = fields.Char(string="Name")
    number = fields.Integer(string="room Number")
