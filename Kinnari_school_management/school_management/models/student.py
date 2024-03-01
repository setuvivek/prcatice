import datetime

from odoo import fields, models , api
from odoo.exceptions import ValidationError
from odoo import _
from odoo.exceptions import UserError

class Student(models.Model):
    _name = "student"
    _description = "Student"
    _rec_name = "gender"
    _order = "roll"



    name = fields.Char(string="Name", required=True )
    roll = fields.Integer(string="Roll", copy =False)
    gender = fields.Selection(selection=[('male','Male'),('female','Female')], string="Gender")
    create_date = fields.Date(string='Today Date', default=lambda s: fields.Date.context_today(s))
    teach_id = fields.Many2one('teacher',string="Select Teacher")
    teacher1_id = fields.Many2many('teacher','teacher1',string="Maths Teacher")
    teacher2_id = fields.Many2many('teacher','teacher2', string="Science Teacher")
    teacher3_id = fields.Many2many('teacher', 'teacher3', string="Physics Teacher")
    enter1 = fields.Float(string="Maths Mark", required=True)
    enter2 = fields.Float(string="Science Mark", required=True)
    enter3 = fields.Float(string="Physics Mark", required=True)
    com = fields.Float(string="Total", compute="_abc",store=True)
    quantity = fields.Float(string="Quantity for order", copy=False)
    stock = fields.Boolean(string="Stock available or not", default=True)
    country_id = fields.Many2one('country', string="Country Name")
    state_id = fields.Many2one('state', string="State Name")
    city_id = fields.Many2one('city', string="City Name")

    @api.depends('enter1','enter2','enter3')
    def _abc(self):
        for record in self:
            record.com = record.enter1 + record.enter2 + record.enter3

    # @api.constrains('roll')
    # def _validate_formula(self):
    #     for record in self:
    #         if record.roll > 0:
    #             raise ValidationError(_('Tag name and.'))

    _sql_constraints = [
        ('name', 'UNIQUE(name)', 'Name Must Be Unique.'),
        ('roll', 'CHECK(age > 0)', 'roll no must be greater than 0.')
    ]







    # create_date = fields.Date(default=datetime.datetime() , readonly=True)

