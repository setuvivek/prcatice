from odoo import models, fields


class SetuSchool(models.Model):
    _name = "setu.school"
    _description ="SetuSchool"
    _rec_name = "name"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(string="Name", tracking=True)
    # city = fields.Char(string="City")
    state = fields.Char(string="State", tracking=True)
    phone = fields.Integer(string="Phone", tracking=True)
    email = fields.Char(string="Email", default="@gmail.com", tracking=True)

    _sql_constraints = [('unique_name','unique(name)','School name should be unique')]




