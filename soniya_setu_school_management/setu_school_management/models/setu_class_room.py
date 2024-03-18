from odoo import models, fields

class ClassRoom(models.Model):

    _name = "setu.class.room"
    _description = "Setu_School"

    name = fields.Char(string='Name')
    room_number = fields.Char(string='Room Number')