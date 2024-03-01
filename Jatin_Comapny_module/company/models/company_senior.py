from odoo import fields, models

class Senior(models.Model):
    _name = "company.senior"
    _description = "senior"

    name = fields.Char(string="Senior Employee Name" , copy=False, required=True)
    work_in = fields.Char(string = "Work In")
    junior_ids = fields.One2many("company.junior", "senior_id", string="Juniors")
    salary = fields.Integer(string="Salary",default="50000")
