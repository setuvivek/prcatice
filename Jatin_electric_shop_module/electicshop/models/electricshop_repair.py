from odoo import fields, models, api

class ElectricshopRepair(models.Model):
    _name = "electricshop.repair"
    _description = "Electricshop Repair"
    _rec_name = 'name'
    # _order = 'date desc'
    name = fields.Char(string="Repairing")
    bill_id = fields.Many2one('electricshop.bill', string="Bill")
    user_id = fields.Many2one('electricshop.user', string="User")
    seller_id = fields.Many2one('electricshop.seller', string="Seller")
    items_id = fields.Many2one('electricshop.items', string="Item")
    description = fields.Char(string='Description Of Repairing')
    items_ids = fields.Many2many('electricshop.items', string="Select Your Product")
    test = fields.Boolean(string='Test')

    # request_from = fields.Char(string="Repairing")
    # bill_idd = fields.Many2one(realted='self.bill_id')

    # @api.depends('bill_id')
    # def _compute_user(self):
    #
    # def click_buttton(self):
    #     if self.bill_id:
    #         self.request_from =True
    #         self.bill_idd = True

    # def button_action(self):
    #     self.test = True


    @api.onchange('bill_id')
    def _onchange_seller_id(self):
        self.seller_id = self.bill_id.seller_id
        self.user_id = self.bill_id.user_id
        self.items_ids = self.bill_id.items_ids

