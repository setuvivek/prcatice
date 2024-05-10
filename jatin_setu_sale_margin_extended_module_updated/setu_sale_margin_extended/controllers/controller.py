from odoo import http


class OdooAcademy(http.Controller):
    @http.route('/academy/subjects/', auth='public', website=True)
    def display_subjects(self, **kw):
        # return "hello setu consulting"
        return http.request.render('setu_sale_margin_extended.subjects', {
            'subjects':
                ['math', 'english', 'science', 'physics', 'chemistry'],
        })

    @http.route('/academy/<int:id>', auth='public', website=True)
    def display_name(self, id):
        return '<h1>{}</h1>'.format(id)

