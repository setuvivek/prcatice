from odoo import fields, models, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit='sale.order'
    
    # def _action_confirm(self):
    #     self.partner_id.setu_credit_limit -= self.amount_total
    #     if self.partner_id.setu_credit_limit < 0:
    #         raise ValidationError("Not Enought credit")

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
