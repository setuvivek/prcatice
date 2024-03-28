from odoo import models, fields

class Team(models.Model):
    _name = 'team'
    _description = 'Team'
    _rec_name = "name"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string='Team Name', required=True)
    owner_id = fields.Many2one("owner", string='Owner')
    players = fields.One2many('player', 'team_id', string='Players')
    city_id = fields.Many2one("city", string="city")
