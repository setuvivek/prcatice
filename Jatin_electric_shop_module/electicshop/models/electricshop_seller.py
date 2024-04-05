from odoo import fields, models, api


class ElectricshopSeller(models.Model):
    _name = "electricshop.seller"
    _description = "Electricshop seller"
    # _rec_name = "no_of_order"
    # _order = 'date desc'
    name = fields.Char(string='Name')
    mobile_no = fields.Char(string="Mobile NO.")
    mail = fields.Char(string="E-Mail", compute='_compute_mail', readonly=False)

    # @api.model_create_multi
    # def create(self, vals_list):
    #     na = self.name
    #     for vals in vals_list:
    #         if not vals.get('mail'):
    #             vals.update({'mail': na+'@gmail.com'})
    #     return super(ElectricshopSeller, self).create(vals_list)

    # @api.model
    # def default_get(self, fields_list):
    #     # EXTENDS base
    #     defaults = super().default_get(fields_list)
    #     # na = str(self.name)
    #     for i in self:
    #         self.mail = i.name+'@gmail.com'
    #     return defaults

    @api.depends('name')
    def _compute_mail(self):
        for i in self:
            nam = str(i.name)
            i.mail = nam + '@gmail.com'

# @api.model
# def default_get(self, fields_list):
#     defaults = super().default_get(fields_list)
#     defaults['age'] = 19
#     return defaults
