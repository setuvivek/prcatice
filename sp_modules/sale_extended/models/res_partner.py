from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
<<<<<<< HEAD

    setu_credit_limit = fields.Integer(string='Credit Limit')
    reward_points = fields.Integer(string='Reward Points')
=======

    setu_credit_limit = fields.Integer(string='Credit Limit',tracking=True)
    reward_points = fields.Float(string='Reward Points',tracking=True)


>>>>>>> 8a8ced84eaef90d32bbeba560bb0401fd2f70720

