from odoo import fields, models, _
from odoo.exceptions import ValidationError


class Order(models.Model):
    _name = "order1"
    _description = "Order_details"
    # _rec_name = "quantity"
    _order = "quantity"

    name = fields.Char(string="Order Name", required=True)
    quantity = fields.Float(string="Quantity for order", copy=False)
    stock = fields.Boolean(string="Stock available or not")

    dos = fields.Date(string="Order Date")
    product_id = fields.Many2one('product', string="Product")

    def unlink(self):
        if self.quantity == 40.00:
            raise ValidationError("You have not access for delete this record")
        rec = super(Order, self).unlink()
        return rec
    # for record in self:
    #     account_ids = self.env['product'].search([('order_id', '=',self.product_id.id)])
    #     account_ids.write({'product_id': record.parent_id.id})
    #
    # super(AccountGroup, self).unlink()

# def write(self,vals):
#        if vals.get('name'):
#            vals.update({'name':'Patel'})
#        rec = super(SetuClass, self).write(vals)
#        return rec
