# -*- coding: utf-8 -*-
# from odoo import http


# class ModuloDario(http.Controller):
#     @http.route('/modulo_dario/modulo_dario', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_dario/modulo_dario/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_dario.listing', {
#             'root': '/modulo_dario/modulo_dario',
#             'objects': http.request.env['modulo_dario.modulo_dario'].search([]),
#         })

#     @http.route('/modulo_dario/modulo_dario/objects/<model("modulo_dario.modulo_dario"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_dario.object', {
#             'object': obj
#         })
