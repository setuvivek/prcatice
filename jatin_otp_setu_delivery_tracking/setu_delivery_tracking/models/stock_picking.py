from odoo import models, fields, _, api
from odoo.exceptions import ValidationError, RedirectWarning
import random
from odoo.addons.whatsapp.tests.common import WhatsAppCommon, MockIncomingWhatsApp


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    random_otp = fields.Char(string="Random OTP", copy=False, readonly=True)
    """
        added by: Jatin Babariya | On : June-05-2024 | Task:OTP Based Validation in Delivery - 259
        use : ADD truck_number Field to add truck number
    """
    truck_number = fields.Char(string="Truck Number")

    """
    added by: Jatin Babariya | On : June-05-2024 | Task:OTP Based Validation in Delivery - 259
    use : To create random number as OTP
    """

    @api.model
    def create(self, vals):
        res = super(StockPicking, self).create(vals)
        for picking in res:
            if picking.picking_type_code == 'outgoing':
                two_dig_otp = random.randint(10, 99)
                four_dig_otp = random.randint(1000, 9999)
                six_dig_otp = str(two_dig_otp) + str(four_dig_otp)
                res.random_otp = six_dig_otp

                #     added by: Jatin Babariya | On : June-17-2024 | Task: OTP Based Validation in Delivery - 259
                #     use : To send otp on customer whatsapp

                setu_wa_template_id = picking.env['whatsapp.template']._find_default_for_model(picking._name)
                res_model = picking._name

                compsoer = picking.env['whatsapp.composer'].create({
                    'wa_template_id': setu_wa_template_id.id,
                    'phone': picking.partner_id.mobile,
                    'res_ids': picking.ids,
                    'res_model': res_model,
                })
                compsoer.action_send_whatsapp_template()
        return res

    """
    added by: Jatin Babariya | On : June-05-2024 | Task: OTP Based Validation in Delivery - 259
    use : To display wizard to verify OTP by clicking on validate button
    """

    def button_validate(self):
        product_qty_list = self.mapped('move_ids_without_package.quantity')
        for picking in self:

            if not self.env.context.get('skip_button', False):
                if sum(product_qty_list):
                    if picking.picking_type_code == 'outgoing' and picking.sale_id:
                        return {
                            'name': _('OTP Verification'),
                            'view_mode': 'form',
                            'res_model': 'otp.verification.wizard',
                            'type': 'ir.actions.act_window',
                            'target': 'new',
                            'context': {'default_picking_id': picking.id},
                        }
        res = super(StockPicking, self).button_validate()
        return res
