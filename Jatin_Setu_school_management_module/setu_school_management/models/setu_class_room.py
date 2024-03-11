from odoo import fields, models

class Class_room(models.Model):
    _name = "setu.class.room"
    _description = "setu_class_room"

    name = fields.Char(string="Name")
    number = fields.Integer(string="Room Number")
