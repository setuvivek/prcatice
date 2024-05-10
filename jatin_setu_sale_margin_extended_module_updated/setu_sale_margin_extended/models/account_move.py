# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = "account.move"

    def action_post(self):
        res = super(AccountMove, self).action_post()

        sale_lines = self.invoice_line_ids.sale_line_ids
        for line in sale_lines:
            if not line.invoice_reference:
                line.invoice_reference = self.payment_reference
            else:
                line.invoice_reference += ", {}".format(self.payment_reference)
        return res

    def button_draft(self):
        sale_lines = self.invoice_line_ids.sale_line_ids
        for line in sale_lines:
            refe = line.invoice_reference
            invoice = refe.split(", ")
            invoice.remove(self.payment_reference)
            line.invoice_reference = ", ".join(invoice)

        res = super(AccountMove, self).button_draft()
        return res
