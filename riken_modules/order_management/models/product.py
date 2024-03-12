from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductData(models.Model):
    _name = "product"
    _description = "Product"


    name = fields.Char(string="product name")
    total_quantity = fields.Integer(string="total quantity")
    date = fields.Date(string="date")
    amt = fields.Char(string="amount")
    p_id = fields.One2many("order", "order_id", string="Product")

    # @api.constrains('total_quantity')
    # def _check_unique_product_name(self):
    #     for record in self:
    #         existing_product = self.env['product'].search([('product_name', '=', record.product_name)])
    #         if len(existing_product) > 1 or (len(existing_product) == 1 and existing_product[0] != record):
    #             raise ValidationError('Product name must be unique!')
    # def _check_quantity_constraint(self):
    #     for product in self:
    #         if product.total_quantity <= 5:
    #             raise ValidationError("Quantity must be greater than 5 for product %s." % product.name)

    _sql_constraints = [('check_total_quantity', 'check(total_quantity >= 5 )', 'The number of total_quantity can\'t be negative.'),
                        ('name_unique', 'unique(name)', 'Product name already exists')]

    # _sql_constraints = [('name_unique', 'unique(name)', 'Product name already exists')]
