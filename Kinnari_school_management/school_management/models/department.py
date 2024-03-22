from odoo  import fields , models, api

class Department(models.Model):
    _name = "department"
    _description = "Department"
    _inherit = ['mail.thread', 'mail.activity.mixin']


    # dep_no = fields.Integer(string="Department Number")
    name1 = fields.Char(string="Name")
    quantity = fields.Float(string="Quantity for order", copy=False)
    stock = fields.Boolean(string="Stock available or not", compute="_abc",store=True)


    @api.depends('quantity','stock')
    def _abc(self):
        for rec in self:
            if rec.quantity > 18:
                rec.stock = True
            else:
                rec.stock = False




