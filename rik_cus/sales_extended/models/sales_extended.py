from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_international_customer = fields.Boolean(string='Is International Customer?',
                                               compute="_compute_is_international_customer",
                                               store=True)

    def _action_confirm(self):
        if self.amount_total > self.partner_id.credit_limit:
            raise ValidationError("ITS MORE THAN 1000 RS SO THIS ORDER IS NOT VALID")



    @api.depends('partner_id')
    def _compute_is_international_customer(self):
        for record in self:
            record.is_international_customer = False
            if record.partner_id.country_id.id != self.env.company.country_id.id:
                record.is_international_customer = True







