from odoo import fields, models, api

class RepairRequestsItems(models.Model):
    _name='repair.requests.items'
    _description='Repair Items'

    name=fields.Char(string='Name',help='Item Name',required=True)
    code=fields.Char(string='Code',help='Unique Code')
    repairable=fields.Boolean(string='Repairable')
    service_type=fields.Selection(selection=[('free', 'Free'),('paid', 'Paid')], string='Service Type',default='free')
    warranty=fields.Selection(selection=[('yes', 'Yes'),('no', 'No')], string='Warranty')
    warranty_period=fields.Integer(string='Warranty Period',help='Warrany Period in Months')

    repair_request_ids=fields.One2many('repair.requests.requests','product_id',string='Repair Requests')
