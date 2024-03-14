from odoo import api, models, fields
from odoo.exceptions import ValidationError
class City(models.Model):

    _name = "city"
    _description = "City"

    city_id = fields.Char(string='City ID', reuired=True, copy=False)
    name = fields.Char(string = 'City Name')
    # district = fields.Char(string = 'District')
    # country = fields.Char(string = 'Country')
    population = fields.Integer(string='Population', required=True)
    pincode = fields.Integer(string='Pincode', required=True)
    state_id = fields.Many2one('state', string='State')
    city_ids = fields.Many2one('country', string='Country')
    # partner_id = fields.One2many('partner', string="City")

    # @api.model
    # def create(self, vals):
    #     if not vals.get('name'):
    #         vals.update({'name':'Ahemdabad'})
    #     rec = super(City, self).create(vals)
    #     return rec


    def unlink(self):
        for rec_id in self:
            if rec_id.name:
                raise ValidationError('This record can not be deleted.')
        return super(City, self).unlink()

    def write(self, vals):
        rec = self.env['state'].search([('name', '=', 'Gujarat')])
        if rec:
            vals.update({'state_id': rec.id})
        res = super(City, self).write(vals)
        return res

    # def write(self, vals):
    #     if vals.get('name'):
    #         vals.update({'name':'jamnagar'})
    #     rec = super(City, self).write(vals)
    #     return rec