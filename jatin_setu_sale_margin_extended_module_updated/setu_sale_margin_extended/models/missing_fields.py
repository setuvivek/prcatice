# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


# added for migration install
class AccountMove(models.Model):
    _inherit = "account.move"
    tax_closing_show_multi_closing_warning = fields.Boolean()


# added for migration install
class AccountPayment(models.Model):
    _inherit = "account.payment"
    client_order_ref = fields.Char(string='Customer Reference', copy=False)

# added for migration install
# class ResPartner(models.Model):
#     _inherit = "res.partner"
#     display_pan_warning = fields.Boolean(string="Display pan warning", compute="_compute_display_pan_warning")

