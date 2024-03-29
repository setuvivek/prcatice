from odoo import fields, models, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit='sale.order'
    
    def _action_confirm(self):
        self.partner_id.setu_credit_limit -= self.amount_total
        if self.partner_id.setu_credit_limit < 0:
            raise ValidationError("Not Enought credit")



