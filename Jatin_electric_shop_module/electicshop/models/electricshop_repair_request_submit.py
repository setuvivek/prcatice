from odoo import fields, models, api

class ElectricshopRepairRequestSubmit(models.Model):
    _name = "electricshop.repair.request.submit"
    _description = "Electricshop Repair"
    # _rec_name = "no_of_order"
    # _order = 'date desc'
    bill_id = fields.Many2one('electricshop.bill', string="Bill")
    user_id = fields.Many2one('electricshop.user', string="User")
    seller_id = fields.Many2one('electricshop.seller', string="Seller")
    items_id = fields.Many2one('electricshop.items', string="Item")
    description = fields.Char(string='Description Of Repairing')
    items_ids = fields.Many2many('electricshop.items', string="Select Your Product")
    repair_id = fields.Many2one('electricshop.repair', string='Repair id')


    @api.onchange('repair_id')
    def _onchange_repair_id(self):
        self.bill_id = self.repair_id.bill_id
        self.seller_id = self.repair_id.seller_id
        self.user_id = self.repair_id.user_id
        self.items_ids = self.repair_id.items_ids
        self.description = self.repair_id.description