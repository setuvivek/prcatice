from odoo import http
from odoo.http import request

class myform(http.Controller):

    @http.route("/form",auth='public')
    def myform(self,id=False,**kw):
        print(id)
        return request.sender("module1.form")