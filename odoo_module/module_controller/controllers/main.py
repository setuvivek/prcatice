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

# """
# This method allows the user to shop for products based on certain criteria.
# def shop(self, page=0, category=None, search='', min_price=0.0, max_price=0.0, ppg=False, **post):
# Parameters:
# - page (int): the page number of the results (default is 0)
# - category (str): the category of products to filter by
# - search (str): the search query to filter products by
# - min_price (float): the minimum price of products to filter by
# - max_price (float): the maximum price of products to filter by
# - ppg (bool): flag to indicate whether to display products per page
# - post (dict): additional parameters passed as key-value pairs
#
# Returns:
# - List of products that match the specified criteria
# """