# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    def action_confirm(self):
        for order in self:
            same_customer = self.search([('partner_id', '=', order.partner_id.id)])
            total_price_subtotal = sum(orders.order_line.price_subtotal for orders in same_customer)
            if total_price_subtotal > order.partner_id.setu_credit_limit:
                raise ValidationError("Customer does not exceeds credit limit....")


        for point in self:
            same_customer = self.search([('partner_id', '=', point.partner_id.id)])
            if same_customer:
                if point.order_line.price_subtotal >= 1000:
                    point.partner_id.setu_reward_points = point.order_line.price_subtotal * 0.02 + point.partner_id.setu_reward_points.id
                else:
                    point.partner_id.setu_reward_points = point.order_line.price_subtotal * 0.01

        return super(SaleOrder, self).action_confirm()



