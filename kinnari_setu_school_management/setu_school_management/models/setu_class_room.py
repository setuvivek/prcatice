from odoo import fields,models , api , _
from odoo.exceptions import ValidationError

class SetuClassRoom(models.Model):
    _name = "setu.class.room"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="name",tracking=True)
    number = fields.Integer(string="Room Number",tracking=True)


    @api.model
    def create(self,vals):
        if not vals.get('number'):
            vals.update({'number':100})
        rec = super(SetuClassRoom,self).create(vals)
        return rec

    def default_get(self, fields):
        res = super(SetuClassRoom, self).default_get(fields)
        res.update({'number': 1})
        return res

    def copy(self,default=None):
        default = dict(default or {})
        default['number'] = self.number + 1
        return super(SetuClassRoom, self).copy(default=default)



    # _sql_constraints = [
    #     ('name_compulsory', 'CHECK(name IS NOT NULL)', 'Name should required'),
    #     ('name_unique', 'unique(name)', "Name Must Be Unique."),
    #     ('size_number', 'CHECK(number>=0)', 'Number field cannot be negative.')
    # ]

    # @api.constrains('number')
    # def write(self, vals):
    #     if not vals.get('number'):
    #         vals.update({'number': 9})
    #     else:
    #         record = self.env['setu.class.room'].search([('number', '=', 15)])
    #         if record:
    #             raise ValidationError(_("The number must between 1 to 15"))
    #     res = super(SetuClassRoom, self).write(vals)
    #     return res








    # def write(self, vals):
    #     if vals.get('number'):
    #         vals.update({'number':5})
    #         res = super(SetuClassRoom, self).write(vals)
    #         return vals

    # @api.constrains('activity_date_deadline_range')
    # def _check_number_range(self):
    #     if any(action.number < 0 for action in self):
    #         raise ValidationError(_("The Number value can't be negative."))
