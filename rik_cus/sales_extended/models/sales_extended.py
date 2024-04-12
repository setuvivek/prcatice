from odoo import fields, models, api, exceptions
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'


    credit_limit = fields.Integer(string='Credit Limit', store=True)
    reedem_code = fields.Boolean(string='Want to use Reward Point?')
    number_of_reward_points = fields.Integer('How many Reward points would you like to use?')



    @api.onchange('number_of_reward_points')
    def _onchange_number_of_reward_points(self):
        for order in self:
            if order.partner_id and order.number_of_reward_points > order.partner_id.setu_reward_point:
                order.number_of_reward_points = order.partner_id.setu_reward_point
                raise ValidationError("You do not have enough reward points.")




    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.number_of_reward_points >= 1:
                order.partner_id.setu_reward_point -= order.number_of_reward_points

                reward_lines = self.env['sale.order.line'].search(
                    [('name', 'ilike', 'reward point'), ('order_id', '=', order.id)])
                if reward_lines:
                    reward_lines.unlink()

                product_name = 'reward point'
                product = self.env['product.template'].search([('name', '=', product_name)],
                                                                     limit=1)
                if product:
                    self.env['sale.order.line'].create({
                        'product_id': product.product_variant_id.id,
                        'order_id': order.id,
                        'name': product.name,
                        'price_unit': -(order.number_of_reward_points),
                        'product_uom_qty': 1,
                    })

            if order.partner_id:
                if order.amount_total > 1000:
                    reward_percentage = 2
                else:
                    reward_percentage = 1
                reward_amount = round(order.amount_total * reward_percentage / 100, 2)
                order.partner_id.setu_reward_point += reward_amount

        return res

    def action_cancel(self):
        res = super(SaleOrder, self)._action_cancel()
        for order in self:
            if order.partner_id:
                if order.amount_total < 1000:
                    reward_percentage = 1
                else:
                    reward_percentage = 2

                reward_deduct = order.amount_total * reward_percentage / 100
                order.partner_id.setu_reward_point -= reward_deduct
        return res


    # @api.model_create_multi
    # def create(self,vals):
    #     # res = super(SaleOrder, self).create(vals)
    #     for order in self:
    #         if  order.product_template_id:
    #             product_name = 'product_template_id'
    #             product = self.env['product.product'].search([('name', '=', product_name)],
    #                                                           limit=1)
    #             if product:
    #                 self.env['sale.order.line'].create({
    #                     'product_id': product.product_variant_id.id,
    #                     'order_id': order.id,
    #                     'name': product.name,
    #                     'product_uom_qty': 1,
    #                 })
    #     super(SaleOrder, self).create(vals)

    # @api.model
    # def create(self, vals):
    #     order = super(SaleOrder, self).create(vals)
    #
    #
    #     if 'sale_product_id' in vals:
    #         sale_product_id = vals['sale_product_id']
    #         product = self.env['product.product'].browse(sale_product_id)
    #
    #
    #         if product:
    #             self.env['sale.order.line'].create({
    #                 'product_id': product.id,
    #                 'order_id': order.id,
    #                 'name': product.name,
    #                 'product_template_id': product.product_tmpl_id.id,
    #                 'product_uom_qty': 1,
    #             })
    #
    #     return order
    # @api.model
    # def create(self, vals):
    #
    #     order = super(SaleOrder, self).create(vals)
    #
    #     product = self.env['product.product'].search([('name', '=', 'Mouse')], limit=1)
    #     if product:
    #
    #         self.env['sale.order.line'].create({
    #             'product_id': product.id,
    #             'order_id': order.id,
    #             'name': product.name,
    #             'product_template_id': product.product_tmpl_id.id,
    #             'product_uom_qty': 1,
    #         })
    #
    #     return order

    # @api.model
    # # def create(self, vals):
    # #
    # #     order = super(SaleOrder, self).create(vals)
    # #
    # #     product = self.env['product.product'].search([('name', '=', 'Mouse')], limit=1)
    # #     if product:
    # #
    # #         order_line_data = {
    # #             'product_id': product.id,
    # #             'order_id': order.id,
    # #             'name': product.name,
    # #             'product_template_id': product.product_tmpl_id.id,
    # #             'product_uom_qty': 1,
    # #         }
    # #
    # #         if vals.get('order_line') and product.name == 'Laptop':
    # #             notebook_page = self.env['new_page'].search([('sale_order_id', '=', False)], limit=1)
    # #             if notebook_page:
    # #                 order_line_data['name'] = notebook_page.name
    # #                 notebook_page.sale_order_id = order.id
    # #
    # #         self.env['sale.order.line'].create(order_line_data)
    # #
    # #     return order

    @api.model
    def create(self, vals):
        order = super(SaleOrder, self).create(vals)

        order_lines = vals.get('order_line', [])
        for line_vals in order_lines:
            product_id = line_vals[2].get('product_id')
            if product_id:
                product = self.env['product.product'].browse(product_id)
                if product:
                    order_line_data = {
                        'product_id': product.id,
                        'order_id': order.id,
                        'name': product.name,
                        'product_template_id': product.product_tmpl_id.id,
                        'product_uom_qty': line_vals[2].get('product_uom_qty', 1),
                    }

                    order_line = self.env['sale.order.line'].create(order_line_data)


                    notebook_page = self.env['product.product'].search([('product_id', '=', product.id)], limit=1)
                    if notebook_page:
                        notebook_page.write({'sale_order_id': order.id})

        return order

    # @api.model
    # def _default_product_template_id(self):
    #     product = self.env['product.product'].search([('name', '=', 'Laptop')], limit=1)
    #     if product:
    #         return product.product_tmpl_id.id
    #     return False
    #
    # product_template_id = fields.Many2one('product.template', string='Product Template', default=_default_product_template_id)
    #


