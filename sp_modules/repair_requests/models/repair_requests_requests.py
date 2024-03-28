from odoo import fields, models, api
from datetime import date
from dateutil.relativedelta import relativedelta


class RepairRequestsRequests(models.Model):
    _name = 'repair.requests.requests'
    _description = 'Repair Request'
    _rec_name = 'customer_name_id'
    _inherit = ['mail.thread', 'mail.activity.mixin']


    customer_name_id = fields.Many2one('repair.requests.customers',string='Customer Name', help='Customer Name', required=True)#many2one
    customer_email = fields.Char(related='customer_name_id.email',string='Customer Email')
    customer_phone = fields.Char(related='customer_name_id.phone', string='Customer Phone')
    product_id = fields.Many2one('repair.requests.items', string='Product', domain=[('repairable', '=', True)])
    remarks=fields.Text(string='Remarks')
    purchase_date = fields.Date(string='Purchase Date',tracking=True)
    warranty_date=fields.Date(string='Warranty Date',compute='_compute_service_type')
    service_type=fields.Selection(selection=[('free', 'Free'),('paid', 'Paid')], string='Service Type',default='free',compute='_compute_service_type',tracking=True)
    service_ids = fields.Many2many('repair.requests.services', string='Additional Service')
                                   #,default=lambda self: self.env['repair.requests.services'].search([('name', '=', 'repair')]).ids)


    @api.model
    def default_get(self,fields):
        res = super(RepairRequestsRequests,self).default_get(fields)
        res['service_ids']=self.env['repair.requests.services'].search([('name', '=', 'repair')]).ids
        return res


    @api.depends('purchase_date','warranty_date')
    def _compute_service_type(self):
        for rec in self:
            if rec.purchase_date:
                rec.warranty_date = rec.purchase_date + relativedelta(months=+self.product_id.warranty_period)
                if rec.warranty_date > date.today() and (self.product_id.warranty == 'yes'):
                    rec.service_type = 'free'
                else:
                    rec.service_type = 'paid'
            else:
                rec.warranty_date = False
                rec.service_type = False

