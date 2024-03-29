from odoo import fields, models, api
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit='sale.order'
    
    def _action_confirm(self):
        if self.amount_total > self.partner_id.setu_credit_limit:
            raise ValidationError("Not Enought credit")



