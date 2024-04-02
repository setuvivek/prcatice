from odoo import fields, models, api
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
<<<<<<< HEAD
    _inherit='sale.order'
    
=======
    _inherit = 'sale.order'

    rewards_use = fields.Boolean(string='Add Reward points')
    reward_point_use = fields.Float(string='Points', tracking=True)

    # def add(self):
    #     for rec in self:
    #         self.env['sale.order.line'].create({'product_id': 40,'order_id':rec.id,'price_unit':-(rec.reward_point_use)})

    @api.onchange('reward_use')
    def _onchange_rewards(self):
        for rec in self:
            if rec.reward_use:
                self.env['sale.order.line'].create({'product_id': 40,'order_id':rec.id,'price_unit':-(rec.reward_point_use)})
            else:
                self.env['sale.order.line'].unlink({'product_id': 40, 'order_id': rec.id})


            # if rec.reward_point_use:
            #     if rec.reward_point_use > rec.partner_id.reward_points:
            #         raise ValidationError('Not Enough Rewards')
            #     else:
            #         pass
            # else:
            #     rec.reward_point_use = False

# @api.onchange('reward_point_use')
#     def _onchange_rewards(self):
#         for rec in self:
#             if rec.reward_point_use:
#                 if rec.reward_point_use > rec.partner_id.reward_points:
#                     raise ValidationError('Not Enough Rewards')
#                 else:
#
#             else:
#                 rec.reward_point_use = False


    # deduction method
>>>>>>> 8a8ced84eaef90d32bbeba560bb0401fd2f70720
    # def _action_confirm(self):
    #     self.partner_id.setu_credit_limit -= self.amount_total
    #     if self.partner_id.setu_credit_limit < 0:
    #         raise ValidationError("Not Enought credit")
<<<<<<< HEAD

    # if rec.amount_total > 1000:
    #     rec.partner_id.reward_points = rec.amount_total * 2 / 100
    # if rec.amount_total > 500 and rec.amount_total < 1000:
    #     rec.partner_id.reward_points = rec.amount_total * 2 / 100

    def action_confirm(self):
        for rec in self:
            search_total = self.search([('partner_id', '=', rec.partner_id.id)])
            sum=0
            for amt in search_total:
                sum+=amt.amount_total
            if sum>rec.partner_id.setu_credit_limit:
                raise ValidationError("Not Enought credit")
        if rec.amount_total > 1000:
            rec.partner_id.reward_points = rec.amount_total * 2 / 100
        if rec.amount_total < 1000 :
            rec.partner_id.reward_points = rec.amount_total * 2 / 100
        return super(SaleOrder,self).action_confirm()

    # def action_confirm(self):
    #     res = super().action_confirm()
    #     partner_id = self.partner_id
    #     sale_order_id = self.browse(54)
    #     filter_line = sale_order_id.order_line.filtered(lambda order_line: order_line.product_template_id.id == 23)
    #     subtotal = sum(filter_line.mapped('price_subtotal'))
    #     return res
=======

    # sum and compare
    # def action_confirm(self):
    #     for rec in self:
    #         search_total = self.search([('partner_id', '=', rec.partner_id.id)])
    #         sum=0
    #         for amt in search_total:
    #             sum+=amt.amount_total
    #         if sum>rec.partner_id.setu_credit_limit:
    #             raise ValidationError("Not Enought credit")
    #     return super(SaleOrder,self).action_confirm()

    # def action_confirm(self):
    #     for rec in self:
    #         search_total = self.search([('partner_id', '=', rec.partner_id.id)])
    #         sum=0
    #         for amt in search_total:
    #             sum+=amt.amount_total
    #         if sum>rec.partner_id.setu_credit_limit:
    #             raise ValidationError("Not Enought credit")
    #     return super(SaleOrder,self).action_confirm()

    # ----------------------------------------------------------------------#rewards

    def action_confirm(self):
        for rec in self:
            # if rec.reward_point_use:
            #     rec.partner_id.reward_points-=rec.reward_point_use
            if rec.amount_total > 1000:
                rec.partner_id.reward_points += rec.amount_total * 2 / 100
            if rec.amount_total < 1000:
                rec.partner_id.reward_points += rec.amount_total * 1 / 100
        return super(SaleOrder, self).action_confirm()

    def action_cancel(self):
        for rec in self:
            cancel_warning = self._show_cancel_wizard()
            if cancel_warning:
                if rec.amount_total > 1000:
                    rec.partner_id.reward_points -= rec.amount_total * 2 / 100
                if rec.amount_total < 1000:
                    rec.partner_id.reward_points -= rec.amount_total * 1 / 100
        return super(SaleOrder, self).action_cancel()

# ----------------------------------------------------------------------

# def action_confirm(self):
#     res = super().action_confirm()
#
#     return res

# def action_confirm(self):
#     res = super().action_confirm()
#     partner_id = self.partner_id
#     sale_order_id = self.browse(54)
#     filter_line = sale_order_id.order_line.filtered(lambda order_line: order_line.product_template_id.id == 23)
#     subtotal = sum(filter_line.mapped('price_subtotal'))
#     return res
>>>>>>> 8a8ced84eaef90d32bbeba560bb0401fd2f70720
