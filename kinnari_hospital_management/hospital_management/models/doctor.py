from odoo import fields, models

class Doctor(models.Model):
    _name = "doctor"
    _description = "Doctor"
    # _rec_name="Specialize"

    name=fields.Char(string="Doctor Name" , required=True)
    gender = fields.Selection(selection=[('male', 'Male'), ('female', 'Female')], string="Gender")
    mobile = fields.Char(string="Mobile")
    address = fields.Char(string="Resident Location")
    degree = fields.Char(string="Doctor Degree" , required=True )
    type = fields.Boolean(string="MD", default=False)
    Specialize = fields.Selection(selection=[('Cardiologists','Cardiologists'),
                                             ('Neurologist','Neurologist'),
                                             ('Dentist','Dentist'),
                                             ('Pediatrician','Pediatrician'),
                                             ('Orthopaedist','Orthopaedist'),
                                             ('Surgeon','Surgeon'),
                                             ('General','General')] , string="Specialize")
    patient_id = fields.One2many('patient','doctor_ids', string="Patient")
    country_id = fields.Many2one('country', string="Country Name")
    state_id = fields.Many2one('state', string="State Name")
    city_id = fields.Many2one('city', string="City Name")


    





