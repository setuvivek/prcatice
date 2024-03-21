from odoo import fields,models

class Section(models.Model):
    _name= "section"
    _description = "Section"
    _rec_name = "type"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name= fields.Char(string="name")
    notes = fields.Text(string='Terms and Conditions')
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

    def create(self,vals):
        if not vals.get('name'):

            a = self.env['staff'].search([('name','=','karan')])
            if a:
                vals.update({'name':'karan'})
        rec = super(Section,self).create(vals)
        return rec





