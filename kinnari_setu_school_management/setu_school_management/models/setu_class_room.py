from odoo import fields,models

class SetuClassRoom(models.Model):
    _name = "setu.class.room"

    name = fields.Char(string="name")
    number = fields.Integer(string="Room Number")

    _sql_constraints = [
        # Partial constraint, complemented by unique index (see below). Still
        # useful to keep because it provides a proper error message when a
        # violation occurs, as it shares the same prefix as the unique index.
        ('name_unique', 'unique(name)', 'Filter names must be unique'),
        ('size_number', 'CHECK(number>=0)', 'Number field cannot be negative.')
    ]
