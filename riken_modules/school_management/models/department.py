from odoo import fields, models

class Department(models.Model):
    _name = "department"
    _description = "Department"

    department = fields.Selection(selection=[("science","SCIENCE"),("math","MATH")], string="Department", required=True)
    teacher_id = fields.Many2one("teacher", string="teacher")
    city_id = fields.Many2one("city", string="City")
    #teacher_id = fields.Many2one("teacher", string="teacher")