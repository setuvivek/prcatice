from odoo import fields, models, api
from odoo.exceptions import ValidationError
class ResPartner(models.Model):
    _inherit='res.partner'

    credit_limit=fields.Integer(string='Credit Limit')







