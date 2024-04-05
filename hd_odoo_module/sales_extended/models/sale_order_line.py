# -*- coding: utf-8 -*-
from odoo import models,fields,api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    extra_price = fields.Float(string='Extra Price')
    previous_price = fields.Float(string='Previous Price')


    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'extra_price')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            tax_results = self.env['account.tax']._compute_taxes([line._convert_to_tax_base_line_dict()])
            totals = list(tax_results['totals'].values())[0]
            amount_untaxed = totals['amount_untaxed']
            amount_tax = totals['amount_tax']

            line.update({
                'price_subtotal': amount_untaxed,
                'price_tax': amount_tax,
                'price_total': amount_untaxed + amount_tax,
            })

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
            price_unit=self.price_unit + self.extra_price,
            quantity=self.product_uom_qty,
            discount=self.discount,
            price_subtotal=self.price_subtotal,
        )

    @api.onchange('product_id', 'order_id.partner_id')
    def onchange_previous_price(self):
        for line in self:
            if line.product_id and line.order_id.partner_id:
                previous_price = self.search([('order_id.partner_id', '=', line.order_id.partner_id.id),
                                              ('product_id', '=', line.product_id.id)], limit=1).id
                line.previous_price = previous_price









