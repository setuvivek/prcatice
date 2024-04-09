from odoo import fields, models, api
import logging

_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    extra_price = fields.Integer(string='Extra Price')

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'extra_price')
    def _compute_amount(self):
        for rec in self:
            res = super(SaleOrderLine, self)._compute_amount()
            rec.price_subtotal += rec.extra_price * rec.product_uom_qty
            rec.price_total = rec.price_subtotal * rec.product_uom_qty
            rec.order_id.amount_untaxed+=rec.extra_price * rec.product_uom_qty
            rec.order_id.amount_total+=rec.price_total
            rec.update({
                'price_subtotal': rec.price_subtotal,
                'price_total': rec.price_total,
            })
            return res

    # def _convert_to_tax_base_line_dict(self):
    #     res = super(SaleOrderLine, self)._convert_to_tax_base_line_dict()
    #     for rec in self:
    #         self.env['account.tax']._convert_to_tax_base_line_dict(
    #             self,
    #             price_unit=rec.price_unit + rec.extra_price,
    #             )
    #     return res
