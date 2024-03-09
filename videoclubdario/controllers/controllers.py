# -*- coding: utf-8 -*-
# from odoo import http


# class Videoclubdario(http.Controller):
#     @http.route('/videoclubdario/videoclubdario', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/videoclubdario/videoclubdario/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('videoclubdario.listing', {
#             'root': '/videoclubdario/videoclubdario',
#             'objects': http.request.env['videoclubdario.videoclubdario'].search([]),
#         })

#     @http.route('/videoclubdario/videoclubdario/objects/<model("videoclubdario.videoclubdario"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('videoclubdario.object', {
#             'object': obj
#         })
