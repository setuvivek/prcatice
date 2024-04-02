from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    setu_credit_limit = fields.Integer(string='Credit Limit')
    reward_points = fields.Integer(string='Reward Points')

