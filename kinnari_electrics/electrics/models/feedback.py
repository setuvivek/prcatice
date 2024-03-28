from odoo import fields,models, api,_
from odoo.exceptions import ValidationError


class Feedback(models.Model):
    _name = "feedback"
    _description = "Feedback"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name_id = fields.Many2one('users', string="Identity Of User", tracking=True)
    user_code = fields.Integer(string="User Unique Code" , related='name_id.code')
    product_code = fields.Integer(string="Product Unique Code", related='name_id.codee')
    production_date = fields.Date(string="Production Date",related='name_id.production_date')
    validity = fields.Date(string="Product Validity" , related='name_id.validity')
    positive = fields.Text(string="Positive Feedback")
    negative = fields.Text(string="Negative Feedback")
    option = fields.Selection(selection=[('replace','replace'),('repair','repair')],string="Option", default="replace")
    reason = fields.Text(string="Write Valid Reason For Replace")
    purchase_date = fields.Date(string="Date For Replacement")
    reason_repair = fields.Text(string="Write valid reason for repair")
    msg = fields.Char(string="msg", readonly = True)


    @api.onchange('validity','purchase_date')
    def onchange_check_date(self):
        for rec in self:
            if rec.validity and rec.purchase_date and rec.validity < rec.purchase_date:
                raise ValidationError(_('You can not replace this item bcz validity became expired', ))


    def replace_item(self):
        self.msg = 'Your Request For Item Replacement Is Accepted'

    def repair_item(self):
        self.msg = 'Your Request For Item Repair Is Accepted'








    # def create(self, vals):
    #     record = self.env['feedback'].search([('name_id','=',self.name_id.id)])
    #     if record:
    #         a = len(record)
    #         vals.update({'number':a})
    #     rec = super(Feedback,self).create(vals)
    #     return rec

        # tarifs = self.env['feedback']
        # self.number = tarifs.search_count([('name_id', '=', self.name_id.id)])
        # return super(Feedback, self).create(vals)
        # for line in self:
        #     record = len(self.env['feedback'].search([('name_id', '=', line.name_id.id)]))
        #     line.number = record


            # line.number = self.search_count([('name_id', '=', line.name_id)])












