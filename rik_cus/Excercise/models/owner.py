from odoo import fields, models

class Owner(models.Model):
    _name = "owner"
    _description = "Owner"
    _rec_name = "owner_name"
    _inherit = ['mail.thread','mail.activity.mixin']

    owner_name = fields.Char(string="Owner name", tracking = True)
    team_name = fields.Char(string="Team_name", tracking = True)
    player_id = fields.One2many("player", "owner_name", string="Players")
    city_id = fields.Many2one("city", string="city", tracking = True)
    state_id = fields.Many2one("state", string="State", tracking = True) # domain = "[('direction', '=', 'city_id')]" domain = "[('direction', '=', 'north')]"
    country_id = fields.Many2one("country", string="Country", tracking = True)
    phone = fields.Integer(string="Phone")
    mail = fields.Char(string="Mail")
