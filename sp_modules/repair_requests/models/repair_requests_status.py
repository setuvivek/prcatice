from odoo import fields, models, api

class RepairRequestsStatus(models.Model):
    _name = 'repair.requests.status'
    _description = 'Repair Request Status'
    _rec_name = ''
    _inherit = ['mail.thread', 'mail.activity.mixin']

    customer_name_id =fields.Many2one('repair.requests.requests',string='Customer')
    # customer_name = fields.Char(string='Customer')
    product = fields.Many2one(related='customer_name_id.product_id',string='Product')
    remarks = fields.Text(related='customer_name_id.remarks',string='Remarks')
    services = fields.Many2many(related='customer_name_id.service_ids',string='Service')
    status=fields.Selection(selection=[('pending', 'Pending'),('complete', 'Complete')], string='Status',default='pending',tracking=True)


    @api.onchange('status')
    def _onchange_status(self):
        for rec in self:
            if rec.status:
                # self.env['repair.requests.requests'].write({'status':rec.status})
                self.customer_name_id.status=rec.status
            else:
                # self.env['repair.requests.requests'].write({'status':False})
                pass
