# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    """
    This model is inherited to add sales profir analysis details.
    """
    _inherit = "sale.order"

    buyer_partner_id = fields.Many2one('res.partner', string="Buyer Name", copy=False)
    sale_partner_id = fields.Many2one('res.partner', string='Salesperson', copy=False)

    buyer_commission_type = fields.Selection([('fixed', 'Fixed'), ('percent', 'Percentage')],
                                             string="Buyer Commision Type")
    buyer_commission_percent = fields.Float("Buyer Commission (%)")
    buyer_commission_value = fields.Float("Buyer Commission")

    sale_commission_type = fields.Selection([('fixed', 'Fixed'), ('percent', 'Percentage')],
                                            string="Sales Commission Type")
    sale_commission_percent = fields.Float("Sales Commission (%)")
    sale_commission_amount = fields.Float("Sales Commision")

    @api.onchange('buyer_commission_type', 'buyer_commission_value', 'buyer_commission_percent',
                  'sale_commission_type', 'sale_commission_amount', 'sale_commission_percent')
    def _onchange_commission_fees(self):
        """
        Use: Update Buyer/Sales commission in sale order line
        """
        for line in self._origin.order_line:
            line._compute_purchase_total()
            line._compute_discount_amount()
            if self.buyer_commission_type == 'fixed':
                line.update({'buyer_commission_type': self.buyer_commission_type,
                             'buyer_commission_value': self.buyer_commission_value})
                line._onchange_buyer_commission_type()
            elif self.buyer_commission_type == 'percent':
                line.update({'buyer_commission_type': self.buyer_commission_type,
                             'buyer_commission_percent': self.buyer_commission_percent})
                line._onchange_buyer_commission_type()
                line._compute_gross_profit()
                line._onchange_buyer_commission_percent()

            if self.sale_commission_type == 'fixed':
                line.update({'sale_commission_type': self.sale_commission_type,
                             'sale_commission_amount': self.sale_commission_amount})
                line._onchange_sale_commission_type()
            elif self.sale_commission_type == 'percent':
                line.update({'sale_commission_type': self.sale_commission_type,
                             'sale_commission_percent': self.sale_commission_percent})
                line._onchange_sale_commission_type()
                line._compute_sales_fees()
                line._onchange_sale_commission_percent()

    @api.constrains('buyer_commission_percent', 'buyer_commission_value', 'sale_commission_percent',
                    'sale_commission_amount')
    def _check_validate_commission_data(self):
        """
        Use: Validate Buyer/Sales Commission Percentage
        """
        if self.buyer_commission_type == 'fixed' and self.buyer_commission_value < 0:
            raise UserError(_('Buyer Commission Value Should be Greater than 0 !!'))
        if self.buyer_commission_type == 'percent' and not (0 <= self.buyer_commission_percent <= 100):
            raise UserError(_('Buyer Commission Percentage Should be Between 0 To 100 !!'))

        if self.sale_commission_type == 'fixed' and self.sale_commission_amount < 0:
            raise UserError(_('Sales Commission Value Should be Greater than 0 !!'))
        if self.sale_commission_type == 'percent' and not (0 <= self.sale_commission_percent <= 100):
            raise UserError(_('Sales Commission Percentage Should be Between 0 To 100 !!'))

    def write(self, vals):
        res = super(SaleOrder, self).write(vals)
        context = self.env.context
        for order in self:
            update_buyer_detail = context.get('update_buyer_detail', True)

            # Buyer Commission Details
            buyer_partner_id = vals.get('buyer_partner_id')
            buyer_commission_type = vals.get('buyer_commission_type')
            buyer_commission_percent = vals.get('buyer_commission_percent')
            buyer_commission_value = vals.get('buyer_commission_value')

            buyer_vals = {}
            if 'buyer_commission_percent' in vals:
                buyer_vals.update({'buyer_commission_percent': buyer_commission_percent})

            if 'buyer_commission_value' in vals:
                buyer_vals.update({'buyer_commission_value': buyer_commission_value})

            if 'buyer_commission_type' in vals:
                buyer_vals.update({'buyer_commission_type': buyer_commission_type})
                if not buyer_commission_type:
                    buyer_vals.update({'buyer_commission_percent': 0.0, 'buyer_commission_value': 0.0})

            if 'buyer_partner_id' in vals and buyer_partner_id:
                buyer_vals.update({'buyer_partner_id': buyer_partner_id})
            elif 'buyer_partner_id' in vals and not buyer_partner_id:
                buyer_vals.update({'buyer_partner_id': buyer_partner_id,
                                   'buyer_commission_type': False,
                                   'buyer_commission_percent': 0.0,
                                   'buyer_commission_value': 0.0})
            if buyer_vals and update_buyer_detail:
                order.with_context(update_buyer_detail=False).update(buyer_vals)
                order.order_line.with_context(update_buyer_detail=False).update(buyer_vals)

            order.order_line._onchange_buyer_commission_type()
            order.order_line._compute_gross_profit()
            if order.buyer_commission_type == 'percent':
                order.order_line._onchange_buyer_commission_percent()

            # Sales Commission Details
            sale_partner_id = vals.get('sale_partner_id')
            sale_commission_type = vals.get('sale_commission_type')
            sale_commission_percent = vals.get('sale_commission_percent')
            sale_commission_amount = vals.get('sale_commission_amount')

            sales_vals = {}
            if vals.get('sale_commission_percent', False):
                sales_vals.update({'sale_commission_percent': sale_commission_percent})

            if 'sale_commission_amount' in vals:
                sales_vals.update({'sale_commission_amount': sale_commission_amount})

            if 'sale_commission_type' in vals:
                sales_vals.update({'sale_commission_type': sale_commission_type})
                if not sale_commission_type:
                    sales_vals.update({'sale_commission_percent': 0.0, 'sale_commission_amount': 0.0})

            if 'sale_partner_id' in vals and sale_partner_id:
                sales_vals.update({'sale_partner_id': sale_partner_id})
            elif 'sale_partner_id' in vals and not sale_partner_id:
                sales_vals.update({'sale_partner_id': sale_partner_id,
                                   'sale_commission_type': False,
                                   'sale_commission_percent': 0.0,
                                   'sale_commission_amount': 0.0})
            if sales_vals and update_buyer_detail:
                order.with_context(update_buyer_detail=False).update(sales_vals)
                order.order_line.with_context(update_buyer_detail=False).update(sales_vals)

            order.order_line._onchange_sale_commission_type()
            order.order_line._compute_sales_fees()
            if order.sale_commission_type == 'percent':
                order.order_line._onchange_sale_commission_percent()
        return res
