from odoo import http
from odoo.http import request


class mycontact(http.Controller):


    @http.route("/mycontact", auth="public")
    def mycontact(self, id=False, **kw):
        s = request.env['res.partner'].sudo().search([])
        # for user in s:
        #     dict.update({count: {'name': user.translated_display_name, 'phone': user.phone,
        #                         'email': user.email, 'company_type': user.company_type}})
        #     count += 1

        return request.render("module1.page", {'recordset': s})

    # @http.route("/Registration_form", auth="public", mode=["post"], csrf=False)
    # def registration_form(self, **post):
    #     Name = post.get("name")
    #     Phone = post.get("phone")
    #     Email = post.get("email")
    #     Company_type = post.get("company_type")
    #
    #     data = request.env["res.partner"].create(
    #         {'name': Name,  'phone': Phone, 'email': Email, 'company_type': Company_type})
    #     return request.redirect("/mycontact")



class RegistrationForm(http.Controller):
    # name = "main.main.main.controller"


    @http.route("/RegistrationForm", auth="public")
    def RegistrationForm(self, id=False, **kw):
        s = request.env['res.partner'].sudo().search([])
        # for user in s:
        #     dict.update({count: {'name': user.translated_display_name, 'phone': user.phone,
        #                         'email': user.email, 'company_type': user.company_type}})
        #     count += 1

        return request.render("module1.registration", {'recordset': s})

    @http.route("/Registration_formm", auth="public", mode=["post"], csrf=False)
    def registration_form(self, **post):
        Name = post.get("name")
        Phone = post.get("phone")
        Email = post.get("email")
        Company_type = post.get("company_type")

        data = request.env["res.partner"].create(
            {'name': Name, 'phone': Phone, 'email': Email, 'company_type': Company_type})
        return request.redirect("/mycontact")
