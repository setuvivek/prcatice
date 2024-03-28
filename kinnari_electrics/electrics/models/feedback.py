from odoo import fields,models, api,_
from odoo.exceptions import ValidationError


class Feedback(models.Model):
    _name = "feedback"
    _description = "Feedback"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name_id = fields.Many2one('users', string="Identity Of User", tracking=True)
    user_name = fields.Char(string="User Name" ,related='name_id.name')
    user_code = fields.Integer(string="User Unique Code" , related='name_id.code')
    product_code = fields.Integer(string="Product Unique Code", related='name_id.codee')
    production_date = fields.Date(string="Production Date",related='name_id.production_date')
    validity = fields.Date(string="Product Validity" , related='name_id.validity')
    positive = fields.Text(string="Positive Feedback")
    negative = fields.Text(string="Negative Feedback")
    replace = fields.Boolean(string="Are You want for replace item?")
    reason = fields.Text(string="Write Valid Reason For Replacement")
    purchase_date = fields.Date(string="Item Purchase Date")
    msg = fields.Char(string="Msg" , readonly= True)

    @api.onchange('validity','purchase_date')
    def _check_dates_(self):
        for rec in self:
            if rec.validity and rec.purchase_date and rec.validity < rec.purchase_date:
                raise ValidationError(_('You can not replace this item bcz validity became expired', ))

    @api.model
    def create(self,vals):
        if vals.get('purchase_date'):
            vals.update({'msg': 'Your Request Successfully Accepted'})
        rec = super(Feedback,self).create(vals)
        return rec



