# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    zakat_percent = fields.Float(string="Zakat")
    sponsor_fee_percent = fields.Float(string="Sponsor Fee")

    def set_values(self):
        """
        This method will set res config settings values.
        """
        super(ResConfigSettings, self).set_values()
        IrDefault = self.env['ir.default'].sudo()
        company_id = self.env.company.id
        IrDefault.set('res.config.settings', 'zakat_percent', self.zakat_percent, company_id=company_id)
        IrDefault.set('res.config.settings', 'sponsor_fee_percent', self.sponsor_fee_percent, company_id=company_id)

    @api.model
    def get_values(self):
        """
        This method will get res config settings values.
        """
        res = super(ResConfigSettings, self).get_values()
        IrDefault = self.env['ir.default'].sudo()
        company_id = self.env.company.id
        zakat_percent = IrDefault._get('res.config.settings', 'zakat_percent', company_id=company_id)
        sponsor_fee_percent = IrDefault._get('res.config.settings', 'sponsor_fee_percent', company_id=company_id)
        res.update(
            zakat_percent=zakat_percent,
            sponsor_fee_percent=sponsor_fee_percent,
        )
        return res
