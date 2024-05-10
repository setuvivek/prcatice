# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class JournalEntryWizard(models.TransientModel):
    """
    This model is created for create journal entry
    """
    _name = "journal.entry.wizard"
    _description = "Journal Entry Wizard"

    date = fields.Date(string="Accounting Date", default=fields.Date.context_today)
    journal_id = fields.Many2one('account.journal', string="Journal")
    partner_id = fields.Many2one('res.partner', string="Customer")
    credit_account_id = fields.Many2one('account.account', string="Credit Account")
    debit_account_id = fields.Many2one('account.account', string="Debit Account")
    amount = fields.Float(string="Amount")
    company_id = fields.Many2one('res.company', string="Company", default=lambda self: self.env.company)

    def create_journal_entry(self):
        """
        This method will create journal entry.
        """
        try:
            context = self.env.context
            type = context.get('type')
            ref = '%s entry' % (type.replace('_', ' '))
            res_id = context.get('active_id', False)
            res_model = context.get('active_model', False)
            label_name = ref
            if res_id and res_model:
                sale_order_line = self.env[res_model].search([('id', '=', res_id)])
                label_name = '%s - %s' % (sale_order_line.order_id.name, sale_order_line.product_id.name)
            vals = {
                'move_type': 'entry',
                'ref': ref.upper(),
                'date': self.date,
                'journal_id': self.journal_id.id,
                'partner_id': self.partner_id and self.partner_id.id or False,
                'line_ids': [
                    (0, 0, {'name': label_name, 'account_id': self.debit_account_id.id,
                            'debit': self.amount, 'partner_id': self.partner_id and self.partner_id.id or False}),
                    (0, 0, {'name': label_name, 'account_id': self.credit_account_id.id,
                            'credit': self.amount, 'partner_id': self.partner_id and self.partner_id.id or False})
                ]
            }
            move_id = self.env['account.move'].create(vals)
            move_id.action_post()
            self.update_reference_from_move(move_id)
        except Exception as err_msg:
            _logger.info("Error coming at the time of creating journal entry. Error: {}".format(err_msg))

    def update_reference_from_move(self, move):
        """
        This method will update move reference in sale order line
        """
        try:
            context = self.env.context
            type = context.get('type')
            order_line = self.env['sale.order.line'].search([('id', 'in', context.get('active_ids'))])
            if type == 'zakat':
                order_line.write({'zakat_reference': move.name,
                                  'zakat_date': move.date})
            if type == 'sponsor_fee':
                order_line.write({'sponsor_fee_reference': move.name,
                                  'sponsor_fee_date': move.date})
            if type == 'buyer_commission':
                order_line.write({'buyer_commission_reference': move.name,
                                  'buyer_commission_date': move.date})
            if type == 'sale_commission':
                order_line.write({'sale_commission_reference': move.name,
                                  'sale_commission_date': move.date})
            if type == 'transport_expense':
                order_line.write({'transport_expense_reference': move.name,
                                  'transport_expense_date': move.date})

        except Exception as err_msg:
            _logger.info("Error coming at the time of updating reference. Error: {}".format(err_msg))
