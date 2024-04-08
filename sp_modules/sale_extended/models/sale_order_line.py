from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    extra_price = fields.Integer(string='Extra Price')


    @api.model
    def create(self,vals):
        res = super(SaleOrderLine,self).create(vals)
        res.price_unit+=res.extra_price
        return res

    # @api.model
    # def write(self,vals):
    #     vals.update({"price_unit": vals.get('price_unit')+vals.get('extra_price')})
    #     # self.price_unit+=self.extra_price
    #     return super(SaleOrderLine,self).write(vals)

    # def _convert_to_tax_base_line_dict(self):
    #     self.env['account.tax']._convert_to_tax_base_line_dict(
    #         self,
    #         partner=self.order_id.partner_id,
    #         currency=self.order_id.currency_id,
    #         product=self.product_id,
    #         taxes=self.tax_id,
    #         price_unit=self.price_unit + self.extra_price,
    #         quantity=self.product_uom_qty,
    #         discount=self.discount,
    #         price_subtotal=self.price_subtotal,
    #     )
    #     return super(SaleOrderLine,self)._convert_to_tax_base_line_dict()


        # for order in self:
        #     order.amount_untaxed += order.extra_price
        # 
        # return super(SaleOrderLine, self)._compute_amounts()


