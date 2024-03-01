from odoo import models, fields

class Department(models.Model):

    _name = "department"
    _description = "Department"



    name = fields.Char(string = 'Name', required = True)
    # dep_ids = fields.Many2one('student', string="Students")
    department_id = fields.Many2one('teacher', string="Teacher")
    city_id = fields.Many2one("city", string="City")



