# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResPartner1(models.Model):
    _inherit = 'res.partner'

    setu_credit_limit = fields.Float(string='Credit Limit')
    setu_reward_points = fields.Float(string='Reward Points', tracking=True)

    is_buyer = fields.Boolean(string='Is Buyer')


    # @api.constrains('order_line')
    # def check_credit_line(self):
    #     for order in self:
    #         total_price_subtotal = sum(orders.price_subtotal for orders in order.order_line)
    #         if total_price_subtotal > order.partner_id.credit_limit:
    #             raise ValidationError("Customer does not exceeds credit limit....")



    # @api.constrains('order_line')
    # def check_credit_line(self):
    #     for i in self:
    #         if sum(i.order.order_line.price_subtotal) > i.partner_id.credit_limit:
    #             raise ValidationError("Customer does not exceeds credit limit....")