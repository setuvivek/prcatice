from odoo import fields, models,api
from odoo.exceptions import ValidationError

class Patient(models.Model):
    _name = "patient"
    _description = "Patient"
    # _rec_name="diseases"

    name = fields.Char(string="Patient Name" , required=True , copy=False)
    age = fields.Integer(string="Age")
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender")
    mobile = fields.Char(string="Mobile")
    address = fields.Boolean(string="You want to add Resident Location")
    diseases= fields.Selection(selection=[('Malaria','Malaria'),
                                          ('Cancer','Cancer'),
                                          ('Chikungunya','Chikungunya')] , string="Diseases")
    doctor_ids = fields.Many2one('doctor' ,string="Doctor")
    doa = fields.Datetime(string="Date of Appointment")
    country_id = fields.Many2one('country', string="Country Name")
    state_id = fields.Many2one('state', string="State Name")
    city_id = fields.Many2one('city', string="City Name")

    @api.model
    def create(self,vals):
        if not vals.get('doctor_ids'):
            rec = self.env['doctor'].search([('Specialize','=','Dentist')])
            if rec:
                vals.update({'doctor_ids':rec.id})
        res = super(Patient,self).create(vals)
        return res

    # @api.constrains('age')
    # def _check_something(self):
    #     for record in self:
    #         if record.age < 18:
    #             raise ValidationError("age must grater than 18")










    # _sql_constraints = [
    #     ('name', 'UNIQUE(name)', 'Name Must Be Unique.'),
    #     ('age', 'CHECK(age > 0)', 'age must be greater than 0.')
    # ]

