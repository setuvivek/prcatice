from odoo import models, fields

class SetuClassRoom(models.Model):
    _name = "setu.class.room"
    _description = "SetuClassRoom"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    number = fields.Integer(string="room Number", tracking=True)
