from odoo import models, fields,api


class Order(models.Model):
    _name = "order"
    _description = "Order"
    # _rec_name = "date"

    owner_name = fields.Char(string="owner name")
    address = fields.Char(string="address")
    date = fields.Datetime(string="date")
    payment= fields.Selection(selection=[('cash','CASH'),('online','ONLINE')],string='payment', default="cash")
    order_id = fields.Many2one("product", string="order")
    order_ids = fields.Many2many("product", string="other product")
    city_id = fields.Many2one("city", string="City")




    status = fields.Selection(string="Status", selection=[('draft', 'DRAFT'), ('done', 'DONE'), ('confirm', 'CONFIRM')],
                              required=False, default="draft")
    # def write(self, vals):
    #     rec = self.env['product'].search([('total_quantity', '=', '10')], limit=1)
    #     if rec:
    #         vals.update({'order_id': rec.id})
    #     res = super(Order, self).write(vals)
    #     return res
    def default_get(self, fields_list):
        defaults = super(Order, self).default_get(fields_list)
        defaults['owner_name'] = 'Tame Kon Heeeee'
        defaults['payment'] = 'cash'
        return defaults

    @api.model
    def create(self, vals):
        # self.search([]).unlink()
        if 'owner_name' not in vals or not vals['owner_name']:
            vals['owner_name'] = 'No Name'
        return super(Order, self).create(vals)


