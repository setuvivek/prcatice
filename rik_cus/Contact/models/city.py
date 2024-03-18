from odoo import fields, models , api

class City(models.Model):
    _name = "city"
    _description = "City"
    _rec_name = "name"

    name = fields.Char(string="city name")
    pincode = fields.Integer(string="pincode", required=True)
    district = fields.Char(string="district name")
    city_id = fields.Many2one("state", string="State", domain = "[('direction', '=', 'north')]") # domain = "[('direction', '=', 'city_id')]"
    city_idd = fields.Many2one("country", string="Country")
    c_id = fields.One2many("customer", "city_id", string="customer")


    status = fields.Selection(string="Status", selection=[('draft', 'DRAFT'), ('done', 'DONE'), ('confirm', 'CONFIRM')],
                              required=False, default="draft")
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get('name'):
                vals.update({'name':'surat'})
        res = super(City, self).create(vals_list)
        return res

        