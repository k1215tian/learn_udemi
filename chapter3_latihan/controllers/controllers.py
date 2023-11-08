# -*- coding: utf-8 -*-
# from odoo import http


# class Chapter2Latihan(http.Controller):
#     @http.route('/chapter2_latihan/chapter2_latihan', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/chapter2_latihan/chapter2_latihan/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('chapter2_latihan.listing', {
#             'root': '/chapter2_latihan/chapter2_latihan',
#             'objects': http.request.env['chapter2_latihan.chapter2_latihan'].search([]),
#         })

#     @http.route('/chapter2_latihan/chapter2_latihan/objects/<model("chapter2_latihan.chapter2_latihan"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('chapter2_latihan.object', {
#             'object': obj
#         })
