from odoo import models, fields


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_quatation = fields.Boolean(string="Is Quatation", default=False)
