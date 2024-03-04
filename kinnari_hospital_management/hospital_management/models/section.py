from odoo import fields,models

class Section(models.Model):
    _name= "section"
    _description = "Section"
    _rec_name = "type"

    type = fields.Selection(selection=[(' Emergency Department',' Emergency Department'),
                                       ('Cardiology Department','Cardiology Department'),
                                       ('Outpatient department (OPD)','Outpatient department (OPD)'),
                                       ('Paramedical Department','Paramedical Department'),
                                       ('Pharmacy Department','Pharmacy Department'),
                                       ('Radiology Department (X-ray)','Radiology Department (X-ray)'),
                                       ('orthopedic department','orthopedic department'),
                                       (' Laboratory Department',' Laboratory Department')] , string="Section Name")

    doctor_id = fields.Many2many('doctor','section1',string="Doctor")
    patient_id = fields.Many2many('patient','section2',string="Patient")
