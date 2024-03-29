# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        for order in self:
            total_price_subtotal = sum(orders.price_subtotal for orders in order.order_line)
            if order.partner_id.setu_credit_limit and total_price_subtotal > order.partner_id.setu_credit_limit and order.partner_id==order.partner_id:
                raise ValidationError("Customer does not exceeds credit limit....")
        return super(SaleOrder, self).action_confirm()

    # @api.constrains('order_line')
    # def check_credit_line(self):
    #     for order in self:
    #         total_price_subtotal = sum(orders.price_subtotal for orders in order.order_line)
    #         if total_price_subtotal > order.partner_id.setu_credit_limit:
    #             raise ValidationError("Customer does not exceeds credit limit....")
