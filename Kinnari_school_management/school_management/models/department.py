from odoo  import fields , models

class Department(models.Model):
    _name = "department"
    _description = "Department"

    # dep_no = fields.Integer(string="Department Number")
    name1 = fields.Char(string="Name")
    quantity = fields.Float(string="Quantity for order", copy=False)
    stock = fields.Boolean(string="Stock available or not", default=True)
    # teacher_ids = fields.Many2many('teacher','teacher1','name1','name', string="Teacher")



