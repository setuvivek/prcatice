# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            total_price_subtotal = sum(orders.price_subtotal for orders in order.order_line)
            if total_price_subtotal > order.partner_id.setu_credit_limit:
                raise ValidationError("Customer does not exceeds credit limit....")

    # @api.constrains('order_line')
    # def check_credit_line(self):
    #     for order in self:
    #         total_price_subtotal = sum(orders.price_subtotal for orders in order.order_line)
    #         if total_price_subtotal > order.partner_id.setu_credit_limit:
    #             raise ValidationError("Customer does not exceeds credit limit....")
