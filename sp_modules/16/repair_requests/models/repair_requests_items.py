from odoo import fields, models, api
from odoo.exceptions import ValidationError

class RepairRequestsItems(models.Model):
    _name='repair.requests.items'
    _description='Repair Items'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    name=fields.Char(string='Name',help='Item Name',required=True)
    code=fields.Char(string='Code',help='Unique Code')
    repairable=fields.Boolean(string='Repairable')
    warranty=fields.Selection(selection=[('yes', 'Yes'),('no', 'No')], string='Warranty',tracking=True,default='yes')
    warranty_period=fields.Integer(string='Warranty Period',help='Warrany Period in Months',default='1')

    repair_request_ids=fields.One2many('repair.requests.requests','product_id',string='Repair Requests')


    def copy(self, default=None):
        default = dict(default or {})
        default.update(name= ("%s (copy)") % self.name,code='')
        return super().copy(default)

    @api.constrains('warranty_period')
    def check_warranty_period(self):
        for rec in self:
            if rec.warranty_period <= 0:
                raise ValidationError('Enter Proper Warranty Period')


    @api.onchange('repairable','warranty')
    def _onchange_repairable(self):
        for rec in self:
            if rec.repairable == False:
                rec.warranty = 'yes'
                rec.warranty_period=1
            if rec.warranty == 'no':
                rec.warranty_period = 1

    
