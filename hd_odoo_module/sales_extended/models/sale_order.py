# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    use_reward_point = fields.Boolean(string='Use Reward Points')
    reward_points = fields.Float(string='Reward Points')

    discount_available = fields.Boolean(string='Discount Available')
    discount = fields.Selection(selection=[('30', '30%'), ('50', '50%'), ('80', '80%')])

 



    def action_confirm(self):
        # for order in self:
        ##order.partner_id.filtered(lambda cus:cus.id == order.partner_id.id)
        #     same_customer = self.search([('partner_id', '=', order.partner_id.id)])
        #     total_price_subtotal = sum(orders.order_line.price_subtotal for orders in same_customer)
        #     if total_price_subtotal > order.partner_id.setu_credit_limit:
        #         raise ValidationError("Customer does not exceeds credit limit....")

        for point in self:
            # order = point.order_line
            for order in point.order_line:
                print('order------------>', order)
                same_customer = self.search([('partner_id', '=', point.partner_id.id)])
                total_price_subtotal = sum(order.mapped('price_subtotal'))
                if same_customer:
                    if total_price_subtotal >= 1000:
                        point.partner_id.setu_reward_points += order.price_subtotal * 0.02
                    else:
                        point.partner_id.setu_reward_points += order.price_subtotal * 0.01

            # add reward point to total price_subtotal--------------------------------------------------
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


            if self.use_reward_point == True:
                if self.reward_points > self.partner_id.setu_reward_points:
                    raise ValidationError("exceeds reward points")
                else:
                    self.order_line = [
                        (0, 0, {'product_id': 42, 'product_uom_qty': 1, 'price_unit': -self.reward_points})]
                    self.partner_id.setu_reward_points -= self.reward_points


            if self.discount_available == True:
                for order in self:
                    if order.discount:
                        order.order_line = [(0, 0, {'product_id': 45})]

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





    #
    # @api.onchange('reward_points', 'use_reward_point')
    # def _onchange_reward_Points(self):
    #     if self.use_reward_point == True:
    #         if self.reward_points > self.partner_id.setu_reward_points:
    #             raise ValidationError("exceeds reward points")
    #         else:
    #             self.order_line = [
    #                 (0, 0, {'product_id': 42, 'product_uom_qty': 1, 'price_unit': -self.reward_points})]
    #             self.partner_id.setu_reward_points -= self.reward_points
    #
    #     else:
    #         i = self.env['sale.order.line'].search([('id', '=', self.id),('product_id', '=', 42)])
    #         i.unlink()
    #         # self.order_line.unlink()



    # @api.onchange('reward_points')
    # def _onchange_reward_points(self):
    #     if self.reward_points > self.partner_id.setu_reward_points:
    #         raise ValidationError("exceeds reward points")
    #     else:
    #         self.order_line = [(0,0,{'product_id':42, 'product_uom_qty':1, 'price_unit': -self.reward_points})]
    #         self.partner_id.setu_reward_points -= self.reward_points

