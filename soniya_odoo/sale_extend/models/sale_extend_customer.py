from odoo import api, models, fields
from odoo.exceptions import ValidationError

class ResPartner(models.Model):

    _inherit = 'res.partner'

    balance = fields.Float(string='Limit')

    # @api.model
    # def get_credit_limit(self, vals):
    #     for records in self:
    #         if not vals.get('balance'):
    #             vals.update({'balance' : '1000'})
    #     return super(ResPartner, self).create(vals)


    # @api.onchange('balance')
    # def check_balance_limit(self):
    #     for recs in self:
    #         if recs.price_subtotal > recs.balance:
    #             raise ValidationError('NO')

