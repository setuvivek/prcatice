from odoo import http
from odoo.http import request

class ContactList(http.Controller):

    @http.route('/contactlist', type='http', auth='public', website=True)
    def contactlist(self, **kw):
        partners = request.env['res.partner'].sudo().search([])
        return http.request.render('module1.page', {
            'partners': partners,
        })

    @http.route('/register', type='http', auth='public', csrf=False, website=True)
    def register(self, **post):
        partner = request.env['res.partner'].sudo().create({
            'name': post.get('name'),
            'phone': post.get('phone'),
            'email': post.get('email'),
            'is_company': post.get('is_company') == 'true',
        })
        return request.redirect('/contactlist')






