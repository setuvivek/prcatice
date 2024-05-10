# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class SaleCommissionWizard(models.TransientModel):
    """
    This model is created for create journal entry
    """
    _name = "sale.commission.wizard"
    _description = "Sales Commission Wizard"

    sale_line_id = fields.Many2one('sale.order.line', string="Sale Line")
    buyer_commission_date = fields.Date(string="Buyer Commission Date")
    buyer_partner_id = fields.Many2one('res.partner', string="Buyer Name")
    buyer_commission_type = fields.Selection([('fixed', 'Fixed'), ('percent', 'Percentage')],
                                             string="Buyer Commision Type")
    buyer_commission_percent = fields.Float("Buyer Commission (%)")
    buyer_commission_value = fields.Float("Buyer Commission")

    sale_commission_date = fields.Date(string="Sales Commission Date")
    sale_partner_id = fields.Many2one('res.partner', string='Salesperson',
                                      default=lambda self: self.env.user.partner_id.id)
    sale_commission_type = fields.Selection([('fixed', 'Fixed'), ('percent', 'Percentage')],
                                            string="Sales Commission Type")
    sale_commission_percent = fields.Float("Sales Commission (%)")
    sale_commission_amount = fields.Float("Sales Commision")

    transport_expense = fields.Float('Transport Expense')
    sponsor_fee_date = fields.Date(string="Sponsor Fee Date")
    zakat_date = fields.Date(string="Zakat Date")

    def update_sale_commission(self):
        context = self.env.context
        res_model = context.get('active_model', False)
        res_id = context.get('active_id', False)

        if res_model and res_id:
            sale_order_line = self.env[res_model].search([('id', '=', res_id)])

            # General information
            sale_order_line.update({
                'transport_expense': self.transport_expense,
                'sponsor_fee_date': self.sponsor_fee_date,
                'zakat_date': self.zakat_date,
            })
            sale_order_line._compute_purchase_total()
            sale_order_line._compute_discount_amount()

            # Buyer Commission Calculation
            sale_order_line.update({
                'buyer_commission_date': self.buyer_commission_date,
                'buyer_partner_id': self.buyer_partner_id.id,
                'buyer_commission_type': self.buyer_commission_type,
                'buyer_commission_percent': self.buyer_commission_percent
            })
            sale_order_line._onchange_buyer_commission_type()
            sale_order_line._compute_gross_profit()
            if self.buyer_commission_type == 'percent':
                sale_order_line._onchange_buyer_commission_percent()
            else:
                sale_order_line.update({'buyer_commission_value': self.buyer_commission_value})

            # Sales Commission Calculation
            sale_order_line.update({
                'sale_commission_date': self.sale_commission_date,
                'sale_partner_id': self.sale_partner_id.id,
                'sale_commission_type': self.sale_commission_type,
                'sale_commission_percent': self.sale_commission_percent
            })
            sale_order_line._onchange_sale_commission_type()
            sale_order_line._compute_sales_fees()
            if self.sale_commission_type == 'percent':
                sale_order_line._onchange_sale_commission_percent()
            else:
                sale_order_line.update({'sale_commission_amount': self.sale_commission_amount})
        return True