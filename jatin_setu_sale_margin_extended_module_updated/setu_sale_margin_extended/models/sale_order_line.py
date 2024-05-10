# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import UserError


class SaleOrderLine(models.Model):
    """
    This model is inherited to add sales commission details.
    """
    _inherit = "sale.order.line"

    invoice_reference = fields.Char(string="Invoice Reference")
    brand_id = fields.Many2one('product.brand', string="Brand", related="product_id.brand_id", store=True)
    purchase_total = fields.Float('Purchase Total', compute="_compute_purchase_total", store="True")
    discount_amount = fields.Float('Product Discount', compute='_compute_discount_amount', store=True)
    gross_profit = fields.Float("Gross Profit", compute='_compute_gross_profit', store=True)
    gross_profit_percent = fields.Float("Gross Profit (%)", compute='_compute_gross_profit', store=True)

    buyer_commission_date = fields.Date(string="Buyer Commission Date", copy=False)
    buyer_partner_id = fields.Many2one('res.partner', string="Buyer Name")
    buyer_commission_type = fields.Selection([('fixed', 'Fixed'), ('percent', 'Percentage')],
                                             string="Buyer Commision Type", copy="False")
    buyer_commission_percent = fields.Float("Buyer Commission (%)", copy=False)
    buyer_commission_value = fields.Float("Buyer Commission", copy=False)

    transport_expense = fields.Float('Transport Expense')

    sponsor_fee_date = fields.Date(string="Sponsor Fee Date", copy=False)
    sponsor_fee = fields.Float("Sponsor Fee", compute='_compute_sales_fees', store=True)

    zakat_date = fields.Date(string="Zakat Date", copy=False)
    zakat = fields.Float("Zakat", compute='_compute_sales_fees', store=True)

    net_profit_amount = fields.Float('Net profit', compute='_compute_sales_fees', store=True)
    net_profit_percent = fields.Float('Net profit (%)', compute='_compute_sales_fees', store=True)
    actual_profit = fields.Float('Actual profit', compute='_compute_actual_profit', store=True)

    sale_commission_date = fields.Date(string="Sales Commission Date", copy=False)
    sale_partner_id = fields.Many2one('res.partner', string='Salesperson', copy=False)
    sale_commission_type = fields.Selection([('fixed', 'Fixed'), ('percent', 'Percentage')],
                                            string="Sales Commission Type", copy="False")
    sale_commission_percent = fields.Float("Sales Commission (%)", copy=False)
    sale_commission_amount = fields.Float("Sales Commision", copy=False)

    # Journal entry reference fields
    zakat_reference = fields.Char(string="Zakat Journal Entry Reference")
    sponsor_fee_reference = fields.Char(string="Sponsor Fee Journal Entry Reference")
    buyer_commission_reference = fields.Char(string="Buyer Commission Journal Entry Reference")
    sale_commission_reference = fields.Char(string="Sales Commission Journal Entry Reference")

    # Sales commission report invoice status identifier
    report_sale_line_invoice_status = fields.Selection(selection=[
        ('draft', 'Draft'), ('posted', 'Posted'),
        ('cancel', 'Cancelled'), ('multiple_invoice', 'Multiple Invoice')],
        string='Report Sale Order Line Invoice Status',
        compute='_compute_report_sale_line_invoice_status', store=True)

    extra_unit_price = fields.Float(string="Extra Price", default=0.0)
    sale_commission_invoice_date = fields.Date(string="Sale Commission Invoice date",
                                               compute="_compute_sale_commission_detail")
    sale_commission_customer_reference = fields.Char(string="Sale Commission Customer Reference",
                                                     compute="_compute_sale_commission_detail")
    transport_expense_date = fields.Date(string="Transport Expense Date", copy=False)
    transport_expense_reference = fields.Char(string="Transport Expense Journal Entry Reference")

    @api.onchange('buyer_commission_type')
    def _onchange_buyer_commission_type(self):
        """
        This method will set buyer commission percentage to 0 for fixed type
        """
        for line in self:
            if line.buyer_commission_type == 'fixed' or line.extra_unit_price:
                line.buyer_commission_percent = 0

    @api.onchange('gross_profit', 'buyer_commission_type', 'buyer_commission_percent', 'extra_unit_price')
    def _onchange_buyer_commission_percent(self):
        """
        This method will calculate sales commission for percentage wise commission type
        """
        for line in self:
            sales_amount = ((line.price_unit + line.extra_unit_price) * line.product_uom_qty)
            if line.extra_unit_price:
                line.buyer_commission_value = line.product_uom_qty * line.extra_unit_price
            if line.buyer_commission_type == 'percent' and line.buyer_commission_percent: # and not line.extra_unit_price:
                line.buyer_commission_value = ((sales_amount * line.buyer_commission_percent) / 100)

    @api.onchange('sale_commission_type')
    def _onchange_sale_commission_type(self):
        """
        This method will set sale commission percentage to 0 for fixed type
        """
        for line in self:
            if line.sale_commission_type == 'fixed':
                line.sale_commission_percent = 0

    @api.onchange('net_profit_amount', 'sale_commission_type', 'sale_commission_percent')
    def _onchange_sale_commission_percent(self):
        """
        This method will calculate sales commission for percentage wise commission type
        """
        for line in self:
            if line.sale_commission_type == 'percent' and line.sale_commission_percent:
                line.sale_commission_amount = ((line.net_profit_amount * line.sale_commission_percent) / 100)

    @api.depends('gross_profit', 'net_profit_amount')
    def _compute_actual_profit(self):
        for line in self:
            line.actual_profit = line.net_profit_amount and (
                    line.net_profit_amount - line.sale_commission_amount) or 0.0

    @api.depends('product_uom_qty', 'discount', 'price_unit')
    def _compute_discount_amount(self):
        """
        This method will calculate product discount in order line
        """
        for line in self:
            line.discount_amount = line.product_uom_qty * (line.price_unit * ((line.discount or 0.0) / 100.0))

    @api.depends('product_uom_qty', 'purchase_price')
    def _compute_purchase_total(self):
        """
        This method will calculate purchase total for order line
        """
        for line in self:
            line.purchase_total = (line.purchase_price * line.product_uom_qty)

    @api.depends('product_uom_qty', 'price_subtotal', 'purchase_price')
    def _compute_gross_profit(self):
        """
        This method will calculate gross profit and gross profir % in order line
        """
        for line in self:
            sales_amount = ((line.price_unit + line.extra_unit_price) * line.product_uom_qty)
            line.gross_profit = (sales_amount - line.purchase_total - line.discount_amount)
            line.gross_profit_percent = line.gross_profit and line.purchase_total and (
                    line.gross_profit / (line.purchase_total * 100)) or 0.0

    @api.depends('gross_profit', 'buyer_commission_type', 'buyer_commission_value')
    def _compute_sales_fees(self):
        """
        This method will calculate zakat, sponsor fee, buyer commission, net profit and net profit %
        """
        IrDefault = self.env['ir.default'].sudo()
        for line in self:
            sales_amount = ((line.price_unit + line.extra_unit_price) * line.product_uom_qty)
            company_id = line.company_id.id
            zakat_percent = IrDefault._get('res.config.settings', 'zakat_percent', company_id=company_id)
            sponsor_fee_percent = IrDefault._get('res.config.settings', 'sponsor_fee_percent', company_id=company_id)
            line.zakat = sales_amount and zakat_percent and (sales_amount * zakat_percent) or 0.0
            line.sponsor_fee = sales_amount and sponsor_fee_percent and (sales_amount * sponsor_fee_percent) or 0.0
            line.net_profit_amount = (
                    line.gross_profit - line.buyer_commission_value - line.transport_expense - line.sponsor_fee - line.zakat)
            line.net_profit_percent = line.net_profit_amount and line.purchase_total and (
                    line.net_profit_amount / (line.purchase_total * 100)) or 0.00

    ######################################
    # Journal Entry Wizard Methods
    ######################################
    def action_journal_entry_zakat(self):
        """ Action define for Zakat fee """
        action = self.get_action_data(type='zakat')
        return action

    def action_journal_entry_sponsor_fee(self):
        """ Action define for Sponsor Fee """
        action = self.get_action_data(type='sponsor_fee')
        return action

    def action_journal_entry_buyer_commission(self):
        """ Action define for Buyer commission """
        action = self.get_action_data(type='buyer_commission')
        return action

    def action_journal_entry_sales_commission(self):
        """ Action define for Sales commission """
        action = self.get_action_data(type='sale_commission')
        return action

    def action_journal_entry_transport_expense(self):
        """ Action define for Sales commission """
        action = self.get_action_data(type='transport_expense')
        return action

    def _check_validation_before_wizard_open(self, type):
        """
        Added By: Mitrarajsinh Jadeja | Date: 14th Apr,2022
        Use: This method will validate selected line
        """
        if len(self.mapped('company_id')) > 1:
            raise UserError(_("Selected Product line are from different company. \n"
                              "Please select product line from one company at a time !!"))

        if type == 'buyer_commission':
            if self.filtered(lambda line: not line.buyer_partner_id):
                raise UserError(_("Some of the product line does not have Buyer(s). \n"
                                  "Please select product line in which buyer is assigned !!"))
            if len(self.mapped('buyer_partner_id').ids) > 1:
                raise UserError(_("Selected Product line having different Buyer(s). \n"
                                  "Please select product line for one buyer at a time !!"))

        if type == 'sale_commission':
            if self.filtered(lambda line: not line.sale_partner_id):
                raise UserError(_("Some of the product line does not have Sales person(s). \n"
                                  "Please select product line in which Sales person is assigned !!"))
            if len(self.mapped('sale_partner_id').ids) > 1:
                raise UserError(_("Selected Product line having different Sales person(s). \n"
                                  "Please select product line for one Sales person at a time !!"))

        if self.env.company.id not in self.mapped('company_id').ids:
            raise UserError(_("Selected Journal / Debit Account / Credit Account are from different company."))

    def get_action_data(self, type):
        """
        Added By: Mitrarajsinh Jadeja | Date: 29th Mar,2022
        Use: This method will validate selected line and open wizard accordingly
        """
        self._check_validation_before_wizard_open(type)

        context = dict(self.env.context or {})
        amount = 0.0
        sale_order_line_exist_journal_entry = False
        if type == 'zakat':
            sale_order_line_exist_journal_entry = self.filtered(lambda line: line.zakat_reference)
            amount = sum(self.mapped('zakat'))
        if type == 'sponsor_fee':
            sale_order_line_exist_journal_entry = self.filtered(lambda line: line.sponsor_fee_reference)
            amount = sum(self.mapped('sponsor_fee'))
        if type == 'buyer_commission':
            sale_order_line_exist_journal_entry = self.filtered(lambda line: line.buyer_commission_reference)
            amount = sum(self.mapped('buyer_commission_value'))
        if type == 'sale_commission':
            sale_order_line_exist_journal_entry = self.filtered(lambda line: line.sale_commission_reference)
            amount = sum(self.mapped('sale_commission_amount'))
        if type == 'transport_expense':
            sale_order_line_exist_journal_entry = self.filtered(lambda line: line.transport_expense_reference)
            amount = sum(self.mapped('transport_expense'))

        if sale_order_line_exist_journal_entry:
            raise UserError(_("You have selected such a product line that has already created a journal entry."
                              " Please select only those product line which has not generated journal entry !!"))
        context.update({'default_amount': amount, 'type': type})
        action = {
            'type': 'ir.actions.act_window',
            'res_model': 'journal.entry.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('setu_sale_margin_extended.journal_entry_wizard_form_view').id,
            'target': 'new',
            'context': context
        }
        return action

    def open_sale_commission_wizard(self):
        context = dict(self.env.context or {})
        context.update({
            'default_sale_line_id': self.id,
            'default_transport_expense': self.transport_expense,
            'default_sponsor_fee_date': self.sponsor_fee_date,
            'default_zakat_date': self.zakat_date,

            'default_buyer_partner_id': self.buyer_partner_id and self.buyer_partner_id.id or False,
            'default_buyer_commission_date': self.buyer_commission_date,
            'default_buyer_commission_type': self.buyer_commission_type,
            'default_buyer_commission_percent': self.buyer_commission_percent,
            'default_buyer_commission_value': self.buyer_commission_value,

            'default_sale_partner_id': self.sale_partner_id and self.sale_partner_id.id or False,
            'default_sale_commission_date': self.sale_commission_date,
            'default_sale_commission_type': self.sale_commission_type,
            'default_sale_commission_percent': self.sale_commission_percent,
            'default_sale_commission_amount': self.sale_commission_amount,

        })

        # Buyer Commission Details
        if self.order_id.buyer_partner_id:
            context.update({'default_buyer_partner_id': self.order_id.buyer_partner_id.id})
            if self.order_id.buyer_commission_type == 'fixed':
                context.update({'default_buyer_commission_type': self.order_id.buyer_commission_type,
                                'default_buyer_commission_value': self.order_id.buyer_commission_value})
            elif self.order_id.buyer_commission_type == 'percent':
                context.update({'default_buyer_commission_type': self.order_id.buyer_commission_type,
                                'default_buyer_commission_percent': self.order_id.buyer_commission_percent})
            else:
                context.update({'default_buyer_commission_type': False,
                                'default_buyer_commission_percent': 0.0, 'default_buyer_commission_value': 0.0})

        # Sales Commission Details
        if self.order_id.sale_partner_id:
            context.update({'default_sale_partner_id': self.order_id.sale_partner_id.id})
            if self.order_id.sale_commission_type == 'fixed':
                context.update({'default_sale_commission_type': self.order_id.sale_commission_type,
                                'default_sale_commission_amount': self.order_id.sale_commission_amount})
            elif self.order_id.sale_commission_type == 'percent':
                context.update({'default_sale_commission_type': self.order_id.sale_commission_type,
                                'default_sale_commission_percent': self.order_id.sale_commission_percent})
            else:
                context.update({'default_sale_commission_type': False,
                                'default_sale_commission_percent': 0.0, 'default_sale_commission_amount': 0.0})

        action = {
            'name': 'Sales Commission',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.commission.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('setu_sale_margin_extended.sale_commission_wizard_form_view').id,
            'target': 'new',
            'context': context
        }
        return action

    @api.depends('invoice_lines.move_id.state')
    def _compute_report_sale_line_invoice_status(self):
        """
        Added By: Mitrarajsinh Jadeja | Date: 2th May,2022
        Use: This method calculate status for report invoice status
        """
        for line in self:
            if len(line.invoice_lines.mapped('move_id')) > 1:
                line.report_sale_line_invoice_status = 'multiple_invoice'
            else:
                line.report_sale_line_invoice_status = line.invoice_lines.move_id.state

    @api.model
    def create(self, vals):
        record = super(SaleOrderLine, self).create(vals)
        if record.order_id.buyer_partner_id:
            record.write({'buyer_partner_id': record.order_id.buyer_partner_id.id})
        if record.order_id.buyer_commission_type:
            record.write({'buyer_commission_type': record.order_id.buyer_commission_type})
        if record.order_id.buyer_commission_percent:
            record.write({'buyer_commission_percent': record.order_id.buyer_commission_percent})
        if record.order_id.buyer_commission_value:
            record.write({'buyer_commission_value': record.order_id.buyer_commission_value})
        record._onchange_buyer_commission_type()
        record._compute_gross_profit()
        if record.buyer_commission_type == 'percent':
            record._onchange_buyer_commission_percent()

        if record.order_id.sale_partner_id:
            record.write({'sale_partner_id': record.order_id.sale_partner_id.id})
        if record.order_id.sale_commission_type:
            record.write({'sale_commission_type': record.order_id.sale_commission_type})
        if record.order_id.sale_commission_percent:
            record.write({'sale_commission_percent': record.order_id.sale_commission_percent})
        if record.order_id.sale_commission_amount:
            record.write({'sale_commission_amount': record.order_id.sale_commission_amount})
        record._onchange_sale_commission_type()
        record._compute_sales_fees()
        if record.sale_commission_type == 'percent':
            record._onchange_sale_commission_percent()
        return record

    @api.depends('extra_unit_price', 'price_unit', 'product_uom_qty')
    def _compute_amount(self):
        super(SaleOrderLine, self)._compute_amount()
        for line in self:
            price = (line.price_unit + line.extra_unit_price) * (1 - (line.discount or 0.0) / 100.0)
            taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty,
                                            product=line.product_id, partner=line.order_id.partner_shipping_id)
            line.update({
                'price_tax': taxes['total_included'] - taxes['total_excluded'],
                'price_total': taxes['total_included'],
                'price_subtotal': taxes['total_excluded'],
            })
            if self.env.context.get('import_file', False) and not self.env.user.user_has_groups(
                    'account.group_account_manager'):
                line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.amount])

    def _prepare_invoice_line(self, **optional_values):
        res = super(SaleOrderLine, self)._prepare_invoice_line()
        for order_line in self:
            res['price_unit'] = (order_line.price_unit + order_line.extra_unit_price)
        return res

    @api.depends('order_id.invoice_ids', 'order_id.invoice_ids.invoice_date', 'order_id.invoice_ids.ref')
    def _compute_sale_commission_detail(self):
        """
        Added By: Mitrarajsinh Jadeja | Date: 2nd June,2022
        Use: This method store invoice date and customer reference
        """
        for order_line in self:
            for invoice_line in order_line.invoice_lines:
                move_id = invoice_line.move_id
                order_line.write({
                    'sale_commission_invoice_date': move_id.invoice_date,
                    'sale_commission_customer_reference': move_id.ref,
                    # 'invoice_reference': move_id.payment_reference,
                })

