from odoo import fields, models, api


class Lead(models.Model):
    _inherit = ['crm.lead',]

    partner_ids = fields.One2many('res.partner', 'parent_id', string='Contact', domain=[('active', '=', True)])

    # iap_enrich_done
    # show_enrich_button









