from odoo import http
from odoo.http import request


class mypage(http.Controller):

    @http.route('/contactlist', type='http', auth='public')
    def mypage(self, *kw):
        channel = request.env['res.partner'].search([], order='id asc')
        return request.render('module_controller.page', {'name': 'Hemangi', 'channel': channel})


@http.route('/submit_registration', type='http', auth='public', methods=['POST'], csrf=False)
def submit_registration(self, **post):
    name = post.get('name')
    email = post.get('email')
    phone = post.get('phone')
    company_type = post.get('company_type')

    partner = request.env['res.partner'].create({
        'name': name,
        'email': email,
        'phone': phone,
        'company_type': company_type,

    })

    return request.redirect("/contactlist")
