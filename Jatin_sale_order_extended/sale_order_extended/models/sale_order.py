from odoo import fields, models, api
from odoo.exceptions import ValidationError, AccessError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_user_international = fields.Boolean(string='User International', store=True,
                                           compute='_compute_is_user_international')

    @api.depends('order_line.price_subtotal', 'order_line.price_tax', 'order_line.price_total',
                 'order_line.extra_unit_price')
    def _compute_amounts(self):
        """Compute the total amounts of the SO."""
        for order in self:
            amount_untaxed = 0
            order_lines = order.order_line.filtered(lambda x: not x.display_type)
            # for j in order.order_line:
            #     total = j.extra_unit_price
            #     order.tax_totals += total
            # amount_untaxed = (sum(order_lines.mapped('price_unit')) + sum(order_lines.mapped('extra_unit_price')))
            for line in order_lines:
                amount_untaxedd = (line.price_unit + line.extra_unit_price) * line.product_uom_qty
                amount_untaxed += amount_untaxedd
            amount_tax = sum(order_lines.mapped('price_tax'))

            order.amount_untaxed = amount_untaxed
            order.amount_tax = amount_tax
            order.amount_total = order.amount_untaxed + order.amount_tax
        return super()._compute_amounts()

    @api.depends('partner_id')
    def _compute_is_user_international(self):
        for rec in self:
            rec.is_user_international = False
            if rec.partner_id.country_id.id != self.env.company.country_id.id:
                rec.is_user_international = True

    def action_confirm(self):
        customer = self.env['res.partner'].browse(self.partner_id.id).setu_money_credit_limit

        for res in self:

            if customer:
                if res.amount_total > customer:
                    #
                    raise ValidationError("your Limit is crossed")
                same_sale_order = self.env['sale.order'].search(
                    [('partner_id', '=', res.partner_id.id),
                     ('state', '=', 'sale')])  # many2one hoy to id thorugh j select thay match thay
                totalamout = sum(res.amount_total for res in same_sale_order)
                if res.amount_total:
                    totalamout += res.amount_total
                    if totalamout > customer:
                        raise ValidationError("customer Limit is crossed")
                    else:
                        res.state = 'sale'

            # points = self.env['res.partner'].browse(self.partner_id.id).setu_reward_point
            if res.state == 'sale':
                partner_id = self.browse(res.id)
                total_amount_list = partner_id.order_line.mapped('price_subtotal')
                total = sum(total_amount_list)
                if total > 999:
                    total_point = total * 2 / 100
                else:
                    total_point = total * 1 / 100
                res.partner_id.setu_reward_point += total_point

            # filter_line = partner_id.order_line.filtered(
            #     lambda order_line: order_line.product_template_id.id).product_template_id.filtered(
            #     lambda general_information: general_information)
            # subtotal = sum(filter_line.mapped('price_subtotal'))

        return super().action_confirm()

    def action_cancel(self):
        for res in self:
            if res.state == 'sale':
                partner_id = self.browse(res.id)
                total_amount_list = partner_id.order_line.mapped('price_subtotal')
                total = sum(total_amount_list)

                if total > 999:
                    total_point = total * 2 / 100
                else:
                    total_point = total * 1 / 100
                res.partner_id.setu_reward_point -= total_point / 2

        return super().action_cancel()
