from odoo import fields, models, api
from odoo.exceptions import MissingError, ValidationError, AccessError
from datetime import date
from dateutil.relativedelta import relativedelta


class ElectricshopBill(models.Model):
    _name = "electricshop.bill"
    _description = "Electricshop Bill"
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    # _rec = "bill_no"
    # _rec_name = "no_of_order"
    # _order = 'date desc'
    name = fields.Char(related="user_id.name")
    bill_no = fields.Integer(string='Bill Number')
    user_id = fields.Many2one('electricshop.user', string='User')
    seller_id = fields.Many2one('electricshop.seller', string='Seller')
    items_ids = fields.Many2many('electricshop.items', string="Select Your Product")
    warranty_to = fields.Date(string="Warranty To")
    warrenty = fields.Char(string='Warranty', compute='_compute_warrenty', store=True)
    warraty_end = fields.Boolean(string="Your Warranty end if want repair then pay extra money?")
    want_repairing = fields.Boolean(string="Want Repairing?")

    @api.depends('warranty_to')
    def _compute_warrenty(self):
        self.warrenty = False
        for rec in self:
            rec.warrenty = relativedelta(rec.warranty_to, date.today()).years
            rec.warrenty = str(rec.warrenty)
            rec.warrenty = rec.warrenty + ' years'

    @api.constrains('warrenty')
    def _check_description(self):
        for record in self:
            if record.want_repairing == True:
                if record.warrenty == '0' + ' years':
                    if record.warraty_end == False:
                        raise ValidationError('Your Warranty is expire!, If you want to repair then pay extra fees!!!'
                                              ' First Tick Checkbox')
                    else:
                        pass
    # @api.model_create_multi
    # def create(self, vals_list):
    #     for vals in vals_list:
    #         if vals.get('warrenty') == 0:
    #             raise ValidationError('Your Wanrrenty End If you want to repair then apy extrafees!!!')
    #
    #     res = super(ElectricshopBill, self).create(vals_list)
    #     return res
