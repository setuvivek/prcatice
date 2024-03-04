from odoo import fields, models

<<<<<<< HEAD
<<<<<<< HEAD
class Department(models.Model):
    _name = "department"
    _description = "Department"

    department = fields.Selection(selection=[("science","SCIENCE"),("math","MATH")], string="Department", required=True)
    teacher_id = fields.Many2one("teacher", string="teacher")
    city_id = fields.Many2one("city", string="City")
    #teacher_id = fields.Many2one("teacher", string="teacher")
=======
=======
>>>>>>> f9de3ec1e5c93553d23e5630558029df4c2060cf

class Department(models.Model):
    _name = 'department'
    _description = 'Department'

    # name = fields.Char(string='Name', required=True)
    name=fields.Selection(selection=[('sports','Sportssss'),('science','Scienceeee')],string='Name')
    hod_id=fields.Many2one('teacher',string='hod')
    members_ids=fields.One2many('teacher','department_id',string='Dept. Members')
<<<<<<< HEAD
>>>>>>> adaac1a1aae6a787e125f2b12070b0ae7a95b81c
=======
=======
class Department(models.Model):
    _name = "department"
    _description = "Department"

    department = fields.Selection(selection=[("science","SCIENCE"),("math","MATH")], string="Department", required=True)
    teacher_id = fields.Many2one("teacher", string="teacher")
    city_id = fields.Many2one("city", string="City")
    #teacher_id = fields.Many2one("teacher", string="teacher")
>>>>>>> 5efbb733230cc2acc5cbaf6822589e04c4cda100
>>>>>>> f9de3ec1e5c93553d23e5630558029df4c2060cf
