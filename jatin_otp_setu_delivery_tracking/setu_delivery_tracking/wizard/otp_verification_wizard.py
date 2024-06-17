from datetime import timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

from odoo import api, exceptions, fields, models, _


class OtpVerificationWizard(models.TransientModel):
    _name = 'otp.verification.wizard'
    _description = 'otp.verification.wizard'

    random_otp = fields.Char("Enter Your OTP")
    picking_id = fields.Many2one('stock.picking')

    """
    added by: Jatin Babariya | On : June-05-2024 | Task: OTP Based Validation in Delivery - 259
    use : if OTP and enterd otp in wizard both are same then continue to validate picking
    """

    def update_info_verify_otp(self):

        picking_id = self.picking_id

        if self.random_otp != picking_id.random_otp:
            raise ValidationError("Your Entered OTP is Wrong, Please Enter valid OTP")
        else:
            return picking_id.with_context({'skip_button': True}, active_ids=picking_id.ids,
                                           active_model=picking_id._name).button_validate()
