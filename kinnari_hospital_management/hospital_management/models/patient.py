from odoo import fields, models

class Patient(models.Model):
    _name = "patient"
    _description = "Patient"
    # _rec_name="diseases"

    name = fields.Char(string="Patient Name" , required=True , copy=False)
    age = fields.Integer(string="Age")
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender")
    mobile = fields.Char(string="Mobile")
    address = fields.Char(string="Resident Location")
    diseases= fields.Selection(selection=[('Malaria','Malaria'),
                                          ('Cancer','Cancer'),
                                          ('Chikungunya','Chikungunya')] , string="Diseases")
    doctor_ids = fields.Many2one('doctor' ,string="Doctor")
    doa = fields.Datetime(string="Date of Appointment", required=True)
    country_id = fields.Many2one('country', string="Country Name")
    state_id = fields.Many2one('state', string="State Name")
    city_id = fields.Many2one('city', string="City Name")








    # _sql_constraints = [
    #     ('name', 'UNIQUE(name)', 'Name Must Be Unique.'),
    #     ('age', 'CHECK(age > 0)', 'age must be greater than 0.')
    # ]

