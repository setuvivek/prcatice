from odoo import fields, models, api


class Player(models.Model):
    _name = "player"
    _description = "Player"
    _rec_name = "name"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Player Name", default="Dhoni", tracking = True)
    team_id = fields.Many2one("team", string="Team Name", tracking = True)
    gender = fields.Selection(selection=[("male","MALE"),("female","FEMALE")], string="Gender")
    nationality = fields.Selection(selection=[("india","INDIA"),("foreigner","FOREIGNER")], string="Nationality")
    owner_name = fields.Many2one("owner", string="Owner Name", tracking = True)
    city_id = fields.Many2one("city", string="city", tracking = True)
    country_id = fields.Many2one("country", string="Country", tracking = True)
    state_id = fields.Many2one("state", string="State", tracking = True)

    display_name = fields.Char(string="Display Name", compute="_compute_display_name", store=True)

    @api.depends('name', 'nationality')
    def _compute_display_name(self):
        for player in self:
            player.display_name = f"{player.name} ({player.nationality})"




    # @api.model_create_multi
    # def write(self, vals):
    #     if 'owner_id' in vals:
    #         owner_name = self.env['player'].browse(vals['owner_id']).name
    #         vals['name'] = "Team of " + owner_name if owner_name else ""
    #     return super(Player, self).write(vals)

    @api.model
    def create(self, vals):
        if vals.get('owner_name'):
            owner = self.env['owner'].browse(vals['owner_name'])
            team = self.env['team'].search([('owner_id', '=', owner.id)], limit=1)
            if team:
                vals['team_id'] = team.id
        return super(Player, self).create(vals)

    def write(self, vals):
        if 'owner_name' in vals:
            owner = self.env['owner'].browse(vals['owner_name'])
            team = self.env['team'].search([('owner_id', '=', owner.id)], limit=1)
            if team:
                vals['team_id'] = team.id
        return super(Player, self).write(vals)



    # @api.onchange('gender')
    # def _onchange_gender(self):
    #     for rec in self:
    #         if rec.gender == "male":
    #             rec.nationality = 'india'
    #         else:
    #             rec.nationality = 'foreigner'






