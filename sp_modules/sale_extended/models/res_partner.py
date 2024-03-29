from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit='res.partner'

    setu_credit_limit=fields.Integer(string='Credit Limit')

    def _action_confirm(self):
        if self.price_total > self.partner_id.setu_credit_limit:
            raise ValidationError("out")
