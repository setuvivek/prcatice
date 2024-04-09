from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    credit_limit = fields.Integer(string='Credit Limit', store=True)
    reedem_code = fields.Boolean(string='Want to use Reward Point?')
    number_of_reward_points = fields.Integer('How many Reward points would you like to use?')



    @api.onchange('number_of_reward_points')
    def _onchange_number_of_reward_points(self):
        for order in self:
            if order.partner_id and order.number_of_reward_points > order.partner_id.setu_reward_point:
                order.number_of_reward_points = order.partner_id.setu_reward_point
                raise ValidationError("You do not have enough reward points.")




    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.number_of_reward_points >= 1:
                order.partner_id.setu_reward_point -= order.number_of_reward_points

                reward_lines = self.env['sale.order.line'].search(
                    [('name', 'ilike', 'reward point'), ('order_id', '=', order.id)])
                if reward_lines:
                    reward_lines.unlink()

                product_name = 'reward point'
                product = self.env['product.template'].search([('name', '=', product_name)],
                                                                     limit=1)
                if product:
                    self.env['sale.order.line'].create({
                        'product_id': product.product_variant_id.id,
                        'order_id': order.id,
                        'name': product.name,
                        'price_unit': -(order.number_of_reward_points),
                        'product_uom_qty': 1,
                    })

            if order.partner_id:
                if order.amount_total > 1000:
                    reward_percentage = 2
                else:
                    reward_percentage = 1
                reward_amount = round(order.amount_total * reward_percentage / 100, 2)
                order.partner_id.setu_reward_point += reward_amount

        return res

    def action_cancel(self):
        res = super(SaleOrder, self)._action_cancel()
        for order in self:
            if order.partner_id:
                if order.amount_total < 1000:
                    reward_percentage = 1
                else:





                    reward_percentage = 2

                reward_deduct = order.amount_total * reward_percentage / 100
                order.partner_id.setu_reward_point -= reward_deduct
        return res





