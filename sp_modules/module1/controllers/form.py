from odoo import http
from odoo.http import request

class myform(http.Controller):

    @http.route("/form",type='http', auth='public', website=True,csrf=False)
    def myform(self, **kw):
        # partners = request.env['res.partner'].sudo().search([])
        # values = {}
        # values.update({
        #     'partners': partners
        # })
        print(kw.get('name'))
        print(kw.get('email'))
        print(kw.get('phone'))
        return request.render("module1.form",{})

