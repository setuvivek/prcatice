# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    is_buyer = fields.Boolean(string="Is Buyer?", copy="False")
    is_sale_person = fields.Boolean(string="Is Sales Person?", copy="False")
