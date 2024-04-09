from odoo import fields, models, api
import logging


_logger = logging.getLogger(__name__)
logging.info("")



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    extra_unit_price = fields.Float(string='Extra Price',store=True)

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


    @api.model
    def create(self, values):
        line = super(SaleOrderLine, self).create(values)
        price_subtotal = (line.price_unit + line.extra_unit_price) * line.product_uom_qty
        line.write({'price_subtotal': price_subtotal})
        return line



# price_unit
# extra_unit_price
# price_subtotal

    # def write(self, values):
    #     if 'price_unit' in values or 'extra_unit_price' in values:
    #         for line in self:
    #             new_subtotal = (values.get('price_unit', line.price_unit) + values.get('extra_unit_price',
    #                                                                                    line.extra_unit_price)) * line.product_uom_qty
    #             values['price_subtotal'] = new_subtotal
    #     return super(SaleOrderLine, self).write(values)






