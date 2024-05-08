# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    use_reward_point = fields.Boolean(string='Use Reward Points')
    reward_points = fields.Float(string='Reward Points')

    discount_available = fields.Boolean(string='Discount Available')
    discount = fields.Selection(selection=[('30', '30%'), ('50', '50%'), ('80', '80%')])

    extra_price = fields.Float(string='Extra Price', compute='_compute_amounts')
    
    buyer_id = fields.Many2one('res.partner', string='Buyer', domain=[('is_buyer', '=', True)])

    weight = fields.Float(string='Total Weight', compute='_compute_amounts')




    def action_confirm(self):
        # for order in self:
        # #order.partner_id.filtered(lambda cus:cus.id == order.partner_id.id)
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


            if self.use_reward_point == True:
                if self.reward_points > self.partner_id.setu_reward_points:
                    raise ValidationError("exceeds reward points")
                else:
                    product_name = self.order_line.filtered(lambda line:line.name == 'reward point' and line.order_id.id == self.id)
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

    @api.depends('order_line.price_subtotal', 'order_line.price_tax', 'order_line.price_total', 'extra_price', 'weight')
    def _compute_amounts(self):
        """Compute the total amounts of the SO."""
        for order in self:
            order_lines = order.order_line.filtered(lambda x: not x.display_type)

            if order.company_id.tax_calculation_rounding_method == 'round_globally':
                tax_results = self.env['account.tax']._compute_taxes([
                    line._convert_to_tax_base_line_dict()
                    for line in order_lines
                ])
                totals = tax_results['totals']
                amount_untaxed = totals.get(order.currency_id, {}).get('amount_untaxed', 0.0)
                amount_tax = totals.get(order.currency_id, {}).get('amount_tax', 0.0)
                extra_price = totals.get(order.currency_id,{}).get('extra_price', 0.0)
                weight = totals.get(order.currency_id,{}).get('weight', 0.0)
                

            else:
                amount_untaxed = sum(order_lines.mapped('price_subtotal'))
                amount_tax = sum(order_lines.mapped('price_tax'))
                extra_price = sum(order_lines.mapped('extra_price'))
                weight = sum(order_lines.mapped('weight'))

            order.amount_untaxed = amount_untaxed
            order.amount_tax = amount_tax
            order.extra_price = extra_price
            order.amount_total = order.amount_untaxed + order.amount_tax + order.extra_price
            order.weight = weight

    @api.onchange('buyer_id')
    def _onchange_buyer(self):
        if self.buyer_id:
            self.order_line.buyer_id = self.buyer_id



