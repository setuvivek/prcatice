from odoo import fields, models , api


class Product(models.Model):
    _name = "product"
    _description = "Product_Table"
    # _rec_name = "incoming"
    _order = "outgoing"

    name = fields.Char(string="Product Name", required=True)
    type = fields.Selection(selection=[('purchase', 'Purchase'), ('sell', 'Sell')], string="Product Type", copy=False)
    date1 = fields.Date(string="Purchase Date")
    date2 = fields.Date(string="Selling Date")
    incoming = fields.Float(string="Quantity for Purchase")
    outgoing = fields.Float(string="Quantity for Sell")
    order_id = fields.One2many('order1','product_id', string="Select Order")

    #
    # @api.constrains('incoming')
    # def _check_date_end(self):
    #     for record in self:
    #         if record.incoming < 0:
    #             raise ValidationError(_("The end date cannot be set in the past"))

    name1 = fields.Char()

    def action_do_something(self):
        for record in self:
            record.name1 = "Something"
        return True
    # com = fields.Float(string="Total", compute="_abc",store=True)

    # c = []
    # def __hash__(self):
    #     if hasattr(self, 'name'):
    # @api.depends('incoming', 'outgoing')
    # def _abc(self):
    #     for record in self:
    #         record.com = record.outgoing - record.incoming



        #
        # for record in self:
        #     all_numbers = [record[fname] for fname in tocheck_fields if fname in record]
        #     all_partners = record._sms_get_default_partners()

#  num_uno=fields.Integer("Value 1")
#  num_dos=fields.Integer('Value 2')
#  campocalculado = fields.Float(string='Calculated field', compute='multiplicar')
#  campocalculado2 = fields.Float(string='Calculated field', compute='dividir')
#
# @api.onchange('num_uno', 'num_dos')
#  def _computeVar(self):
#      for record in self:
#          record.multiplicar = record.num_uno * record.num_dos
#          record.dividir = record.num_dos / record.num_uno
# num_uno=fields.Integer("Value 1")
# num_dos=fields.Integer('Value 2')
# multiplicar = fields.Float(string='Multiplicar', compute='_computeVar')
# dividir = fields.Float(string='Dividir field', compute='_computeVar')
#
# @api.depends('num_uno', 'num_dos')
# def _computeVar(self):
#     for record in self:
#         record.multiplicar = record.num_uno * record.num_dos
#         record.dividir = record.num_dos / record.num_uno

# from odoo import api, fields, models
#
# class TestComputed(models.Model):
#     _name = "test.computed"
#
#     total = fields.Float(compute="_compute_total")
#     amount = fields.Float()
#
#     @api.depends("amount")
#     def _compute_total(self):
#         for record in self:
#             record.total = 2.0 * record.amount
