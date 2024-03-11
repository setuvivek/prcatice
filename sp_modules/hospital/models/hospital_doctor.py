from odoo import fields, models


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'All Doctor'
    _order = 'name'  # type

    name = fields.Char(string='Name', help='Name of Doctors')
    code = fields.Char(string='Code',help='unique Code')
    dept=fields.Many2one('hospital.dept',string='Department',help='Department of Doctor')
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string='Gender')
    phone = fields.Char(string='Phone', unaccent=False)
    email = fields.Char(string='Email')
    shift = fields.Selection(string='Shift', selection=[('morning', 'Morning'), ('night', 'Night')], default='morning')
    type=fields.Selection(selection=[('permanent', 'Permanent'), ('visiting', 'Visiting')], string='Type',default='permanent')
    city_id = fields.Many2one('city',string='City')
    state_id = fields.Many2one('state', string='State')
    country_id = fields.Many2one('country', string='Country')
    surgeon=fields.Boolean(string='Surgeon')
    avl = fields.Boolean(string='Availability')

    _sql_constraints = [('code_unique', 'unique(code)', 'Use different Code'),('name_check', 'CHECK(name IS NOT NULL and code IS NOT NULL)', 'Name and Code field cant be Empty')]
    # _sql_constraints = []


