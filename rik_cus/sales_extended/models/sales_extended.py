from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # is_international_customer = fields.Boolean(string='Is International Customer?',
    #                                            compute="_compute_is_international_customer",
    #                                            store=True)
    credit_limit = fields.Integer(string='Credit Limit', store=True)
    reedem_code = fields.Boolean(string='Want to use Reward Point?')
    number_of_reward_points = fields.Integer('How many Reward points would you like to use?')

    # _sql_constraints = [('reward_points', 'number_of_reward_points > setu_reward_point', 'Not Valid')]

    @api.constrains('number_of_reward_points')
    def _constrains_reward_points(self):
        for order in self:
            if order.partner_id:
                if order.number_of_reward_points > order.partner_id.setu_reward_point:
                    raise ValidationError("Not Enough Reward Points in your Balance")
    def _action_cancel(self):
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

    def _action_confirm(self):
        res = super(SaleOrder, self)._action_confirm()
        for order in self:
            if order.partner_id:
                if order.amount_total < 1000:
                    reward_percentage = 1
                else:
                    reward_percentage = 2

                reward_amount = order.amount_total * reward_percentage / 100
                reward_amount = round(reward_amount, 2)
                order.partner_id.setu_reward_point += reward_amount
        return res

    # def create(self):
    #     for order in self:
    #         if order.number_of_reward_points:
    #             order.orderline.price_unit - order.number_of_reward_points
    #
    #









    # def _action_confirm(self):
    #     res = super(SaleOrder, self).action_confirm()
    #     for order in self:
    #         if order.partner_id and order.partner_id.credit_limit:
    #             reward_percentage = 0.01 if order.amount_total < 1000 else 0.02
    #             reward_amount = order.amount_total * reward_percentage
    #             order.partner_id.setu_reward_point += reward_amount
    #     return res


    # def _action_confirm(self):
    #     res = super(SaleOrder, self)._action_confirm()
    #     for order in self:
    #         if order.partner_id:
    #             if order.amount_total < 1000:
    #                 reward_percentage = 0.01
    #             else:
    #                 reward_percentage = 0.02
    #
    #             reward_amount = order.amount_total * reward_percentage
    #             order.partner_id.setu_reward_point += reward_amount
    #     return res



    # def _action_confirm(self):
    #     for order in self:
    #         total_amount = 0
    #         sale_orders = self.env['sale.order'].search([('partner_id', '=', order.partner_id.id)])
    #         for sale_order in sale_orders:
    #             total_amount += sale_order.amount_total
    #
    #         if total_amount > order.partner_id.credit_limit:
    #             raise ValidationError("Order cannot be confirmed as it exceeds the credit limit for this customer")



    # @api.depends('partner_id')
    # def _compute_is_international_customer(self):
    #     for record in self:
    #         if record.partner_id.country_id.id != self.env.company.country_id.id:
    #             record.is_international_customer = True



































#
    # def _action_confirm(self):
    #     for order in self:
    #         if order.amount_total > order.partner_id.credit_limit:
    #             raise ValidationError("Order cannot be confirmed as it is more than credit limit for this customer")


 # def _action_confirm(self):
    #     if self.amount_total > 900:
    #         raise ValidationError("ITS MORE THAN 900 RS SO THIS ORDER IS NOT VALID")


 # if self.amount_total > self.partner_id.credit_limit:
 #                raise ValidationError("Order amount exceeds credit limit for this customer")




# def _action_confirm(self):
    #     for order in self:
    #         total_amount = sum(order.amount_total for order in self.env['sale.order'].search([
    #             ('partner_id', '=', order.partner_id.id),
    #         ]))
    #         if total_amount > order.partner_id.credit_limit:
    #             raise ValidationError("Order cannot be confirmed as it exceeds the credit limit for this customer")








