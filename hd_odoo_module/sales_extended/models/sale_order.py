# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    use_reward_point = fields.Boolean(string='Use Reward Points')
    reward_points = fields.Float(string='Reward Points')


    def action_confirm(self):
        # for order in self:
        #     same_customer = self.search([('partner_id', '=', order.partner_id.id)])
        #     total_price_subtotal = sum(orders.order_line.price_subtotal for orders in same_customer)
        #     if total_price_subtotal > order.partner_id.setu_credit_limit:
        #         raise ValidationError("Customer does not exceeds credit limit....")


        for point in self:
            # order = point.order_line
            for order in point.order_line:
                print('order------------>',order)
                same_customer = self.search([('partner_id', '=', point.partner_id.id)])
                total_price_subtotal = sum(order.mapped('price_subtotal'))
                if same_customer:
                    if total_price_subtotal >= 1000:
                        point.partner_id.setu_reward_points += order.price_subtotal * 0.02
                    else:
                        point.partner_id.setu_reward_points += order.price_subtotal * 0.01

            #add reward point to total price_subtotal--------------------------------------------------
            # for product in self:
            #     list = []
            #     for p1 in product.order_line:
            #         if product.reward_points:
            #             list.append({
            #                 'product_id': 42,
            #                 'product_uom_qty': 1,
            #                 'price_unit': -self.reward_points,
            #                 'order_id': self.id
            #
            #             })
            # self.env['sale.order.line'].create(list)
            if self.reward_points > self.partner_id.setu_reward_points:
                raise ValidationError("exceeds reward points")
            else:
                self.order_line = [(0, 0, {'product_id': 42, 'product_uom_qty': 1, 'price_unit': -self.reward_points})]
                self.partner_id.setu_reward_points -= self.reward_points


            return super(SaleOrder, self).action_confirm()

    def action_cancel(self):
        res = super(SaleOrder, self).action_cancel()
        cancel_warning = self._show_cancel_wizard()
        if cancel_warning:
            for line in self:
                for order in line.order_line:
                    total_price_subtotal = sum(order.mapped('price_subtotal'))
                    same_customer = self.search([('partner_id', '=', line.partner_id.id)])
                    if same_customer:
                        if total_price_subtotal >= 1000:
                            line.partner_id.setu_reward_points -= order.price_subtotal * 0.02
                        else:
                            line.partner_id.setu_reward_points -= order.price_subtotal * 0.01

            if self.reward_points < self.partner_id.setu_reward_points:
                self.partner_id.setu_reward_points += self.reward_points


        return res
    


    # @api.onchange('reward_points')
    # def _onchange_reward_points(self):
    #     if self.reward_points > self.partner_id.setu_reward_points:
    #         raise ValidationError("exceeds reward points")
    #     else:
    #         self.order_line = [(0,0,{'product_id':42, 'product_uom_qty':1, 'price_unit': -self.reward_points})]
    #         self.partner_id.setu_reward_points -= self.reward_points

    # @api.onchange('reward_points')
    # def _onchange_reward_points(self):
    #     for rec in self:
    #         if rec.reward_points > rec.partner_id.setu_reward_points:
    #             raise ValidationError("exceeds reward points")
    #         else:
    #             res = rec.reward_points
    #             if res:
    #                 orders_line = {'product_id': 42, 'product_uom_qty': 1, 'price_unit': -rec.reward_points}
    #                 rec.env['sale.order.line'].create(orders_line)
    #                 rec.partner_id.setu_reward_points -= rec.reward_points


