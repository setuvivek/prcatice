from odoo import api, models, fields
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):

    _inherit = 'sale.order'

    credit_limit = fields.Float(string='Credit Limit', default = 1000)

    # @api.onchange('product_template_id')
    # for records in 'product_template_id':
    #     if 'sale.order.line.price_subtotal' > 1000:
    #         raise ValidationError('you can purchase the item till 1000')

    # @api.model
    # def default_get(self, fields_list):
    #     default = super(SaleOrder, self).default_get(fields_list)
    #     default['credit_limit'] = 1000
    #     return default

    # @api.onchange('partner_id', 'price_subtotal')
    # def onchange_price_subtotal(self):
    #     for records in self:
    #         total_amount = sum(records.sale.order.line.price_subtotal for records in self.product_template_id)
    #         if total_amount > self.credit_limit:
    #             raise ValidationError('_____')

    # def action_done(self):
    #     for records in self:
    #         if records.price_subtotal > records.credit_limit:
    #             raise ValidationError('_')

    def action_confirm(self):
        for records in self:
            if records.partner_id.balance:
                total_amount = sum(records.amount_total for records in self.env['sale.order'].search([('partner_id', '=', records.partner_id.id)]))

                if total_amount + records.amount_total > records.partner_id.balance:
                    raise ValidationError('Your credit limit is less than your total amount.')

    # def action_confirm(self):
    #     for order in self:
    #         if order.partner_id.balance:
    #             total_order = sum(order.partner_id)


    # def action_confirm(self):
    #     for order in self:
    #         if order.partner_id.balance:
    #             total_order = self.env['sale.order'].search([('partner_id', '=', order.partner_id.id)])
    #
    #             total_amount = sum(order.amount_total for order in self.env['sale.order'].search([('partner_id', '=', order.partner_id.id)]))
    #
    #             if total_amount + order.amount_total > order.partner_id.balance:
    #                 raise ValidationError('Your credit limit is less than your total amount.')
    #     return super(SaleOrder, self).action_confirm()