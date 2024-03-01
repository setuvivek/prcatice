from odoo import fields, models

class Department(models.Model):
    _name = "department"
    _description = "Department"

    name = fields.Char(string="Department", required=True)
    hod = fields.Char(string="H.O.D.")
    teacher_ids = fields.One2many("teacher", "department_id", string="Add New Teacher")
    select_teacher_add_ids = fields.Many2many("teacher", string="Select existing Teacher")