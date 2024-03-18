from odoo import models, fields

class SetuAdmissionForm(models.Model):
    _name = "setu.admission.form"
    _description = "SetuAdmissionForm"
    _rec_name = "student_name"

    student_name = fields.Char(string="Student Name")
    class_id = fields.Many2one("setu.class", string="Class")
    address = fields.Char(string="Address")
    email = fields.Char(string="Email")
    phone = fields.Integer(string="Phone")
    dob = fields.Date(string='DOB')
    state = fields.Char(string="State")

    status=fields.Selection(string="Status", selection=[('draft','DRAFT'),('done','DONE'),('confirm','CONFIRM')], required=False, default="draft")

    # def action_done(self):
    #     self.env['setu.admission.form'].create({'student_name':'Riken'})