from odoo import http
from odoo.http import request

class PartnerRegistration(http.Controller):

    @http.route('/partner/register', type='http', auth='public', website=True)
    def partner_register_form(self, **kw):
        return http.request.render('module1.partner_register_template', {})

    @http.route('/partner/register', type='http', auth='public', website=True, methods=['POST'])
    def partner_register_submit(self, **post):
        if post.get('name') and post.get('email'):
            Partner = request.env['res.partner']
            Partner.create({
                'name': post.get('name'),
                'email': post.get('email'),
                'phone': post.get('phone')
            })
            return request.redirect('/partner/thank-you')
        else:
            error_message = "Error: Name and Email are required fields"
            return http.request.render('module1.partner_register_template', {'error_message': error_message})
# class ContactList(http.Controller):
#
#     @http.route('/contactlist', type='http', auth='public', website=True)
#     def contactlist(self, **kw):
#         partners = request.env['res.partner'].sudo().search([])
#         return http.request.render('module1.page', {
#             'partners': partners,
#         })


# from odoo import http
# from odoo.http import request
#
#
# class contactlist(http.Controller):
# #
# #     # @http.route("/contactlist",auth="public")
# #     # def contactlist(self,*kw):
# #     #     return request.render("module1.page",{'name':'Riken'})
# #
#     @http.route('/contactlist', type='http', auth='public', website=True)
#     def contactlist(self, **kw):
#         partners = request.env['res.partner'].sudo().search([])
#         return http.request.render('module1.page', {
#             'partners': partners,
#         })
#
