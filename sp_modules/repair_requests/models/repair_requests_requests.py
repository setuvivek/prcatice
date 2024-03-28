from odoo import fields, models, api
from dateutil.relativedelta import relativedelta


class RepairRequestsRequests(models.Model):
    _name = 'repair.requests.requests'
    _description = 'Repair Request'
    _rec_name = 'customer_name_id'

    customer_name_id = fields.Many2one('repair.requests.customers',string='Customer Name', help='Customer Name', required=True)#many2one
    customer_email = fields.Char(related='customer_name_id.email',string='Customer Email')
    customer_phone = fields.Char(related='customer_name_id.phone', string='Customer Phone')
    product_id = fields.Many2one('repair.requests.items', string='Product', domain=[('repairable', '=', True)])
    purchase_date = fields.Date(string='Purchase Date')
    warranty_date=fields.Date(string='Warranty Date')#,compute='_compute_warranty_date')
    service_ids = fields.Many2many('repair.requests.services', string='Additional Service')
                                   #,default=lambda self: self.env['repair.requests.services'].search([('name', '=', 'repair')]).ids)

    service_type=fields.Selection(related='product_id.service_type')

    @api.model
    def default_get(self,fields):
        res = super(RepairRequestsRequests,self).default_get(fields)
        res['service_ids']=self.env['repair.requests.services'].search([('name', '=', 'repair')]).ids
        return res


    @api.depends('purchase_date')
    def _compute_warranty_date(self):
        for rec in self:
            rec.warranty_date = rec.purchase_date + relativedelta(months=+1)
