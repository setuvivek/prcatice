import json
from odoo import http
from odoo.http import request


class Loginuser(http.Controller):

    @http.route("/Setuleadform", auth="public", website=True)
    def SetuLeadForm(self, **kw):
        return request.render("website_sale_extended.contact_us_form", {})

    @http.route(['/productgetqty'], type='json', auth='user', website=True)
    def productGetQty(self,data=False, **kw):
        prod = request.env['stock.quant'].search([('product_id','=',int(data)),('location_id.usage','=', 'internal')])
        return {'stock_loc':prod.location_id.display_name,'qty':prod.mapped('quantity')}

    @http.route("/Setu_Lead_Form", auth="public", mode="[post]", csrf=False, website=True)
    def SetuLeadFormm(self, **post):
        Name = post.get("name")
        Phone = post.get("phone")
        Company = post.get("partner_name")
        Product = post.get("contact5")
        Question = post.get("contact_name")
        # Type = post.get("type")

        request.env['crm.lead'].create(
            {'name': Name, 'phone': Phone, 'partner_name': Company, 'city': Product, 'contact_name': Question,
             })
        return request.render("website_sale_extended.submit_lead_thanks")

    # @http.route("/show_location_stock", auth="public", website=True)
    # def ShowLocaitonStock(self, id=False, **kw):
    #     s = request.env['stock.quant'].sudo().search([('product_id.id', '=', 36)])
    #     return request.render("website_sale_extended.stock", {'recordset': s})
