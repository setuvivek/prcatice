from odoo import fields, models

class Student_cast(models.Model):
    _name = "setu.student.cast"
<<<<<<< HEAD
    _inherit = ['mail.thread', 'mail.activity.mixin']
=======
    _description = "Setu Student Cast"
>>>>>>> 0c53dcac5aa5f8ad5e4668828bd4bbe6b6c4ec57

    name = fields.Char(string="Name")
