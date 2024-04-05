from odoo import fields, models, api


class Partner(models.Model):
    _inherit = "res.partner"

    setu_money_credit_limit = fields.Integer(string="Credit Limit", default='1000')
    setu_reward_point = fields.Float(string="Reward Points")

    # @api.onchange('partner_id')
    # def _onchange_percentage_amount(self):
    #     totalamo = self.env['sale.order'].search(
    #         [('state', '=', 'sale'), ('partner_id', '=', self.partner_id.id)])
    #     totalamout = sum(self.env['sale.order'].percentage_amount_total for self in totalamo)
    #     self.setu_reward_point = totalamout
    # @api.model
    # def default_get(self, fields_list):
    #     # EXTENDS base
    #     defaults = {} or None
    #     res = super().default_get(fields_list)
    #
    #     defaults['setu_money_credit_limit'] = 1000
    #     return res
