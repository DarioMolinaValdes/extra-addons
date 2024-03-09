# -*- coding: utf-8 -*-
# from odoo import http


# class GreenHarvest(http.Controller):
#     @http.route('/green_harvest/green_harvest', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/green_harvest/green_harvest/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('green_harvest.listing', {
#             'root': '/green_harvest/green_harvest',
#             'objects': http.request.env['green_harvest.green_harvest'].search([]),
#         })

#     @http.route('/green_harvest/green_harvest/objects/<model("green_harvest.green_harvest"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('green_harvest.object', {
#             'object': obj
#         })
