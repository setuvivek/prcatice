from odoo import fields, models

class Junior(models.Model):
    _name = "company.junior"
    _description = "junior"

    name = fields.Char(string="Junior Employee Name" , required=True, copy=False) #required pela hoy to duplicate ma copy work na kare&& copy pela hoy to error ave duplicate karie to
    join_date = fields.Date(string="Joining Date")
    work_in = fields.Char(string = "Work In")
    senior_id = fields.Many2one("company.senior", string = "Work Under")
    salary = fields.Integer(string="Salary" ,default="20000")
    city_id = fields.Many2one("city",string="City")