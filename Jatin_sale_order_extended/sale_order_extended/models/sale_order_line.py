from odoo import fields, models, api


# from odoo.exceptions import ValidationError, AccessError


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    extra_unit_price = fields.Float(string="extra_unit_price")

    def _convert_to_tax_base_line_dict(self):
        """ Convert the current record to a dictionary in order to use the generic taxes computation method
        defined on account.tax.

        :return: A python dictionary.
        """
        self.ensure_one()
        return self.env['account.tax']._convert_to_tax_base_line_dict(
            self,
            partner=self.order_id.partner_id,
            currency=self.order_id.currency_id,
            product=self.product_id,
            taxes=self.tax_id,
            price_unit=self.price_unit + self.extra_unit_price,
            quantity=self.product_uom_qty,
            discount=self.discount,
            price_subtotal=self.price_subtotal,

        )
        return super()._convert_to_tax_base_line_dict()


    @api.depends('product_uom_qty', 'price_unit', 'extra_unit_price')
    def _compute_amount(self):
        for line in self:
            line.price_subtotal = (line.price_unit + line.extra_unit_price) * line.product_uom_qty
        return super()._compute_amount()
