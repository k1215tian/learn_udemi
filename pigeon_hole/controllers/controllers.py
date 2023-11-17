# -*- coding: utf-8 -*-
from odoo import http

# class PigeonHole(http.Controller):
#     @http.route('/pigeon_hole/pigeon_hole/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pigeon_hole/pigeon_hole/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pigeon_hole.listing', {
#             'root': '/pigeon_hole/pigeon_hole',
#             'objects': http.request.env['pigeon_hole.pigeon_hole'].search([]),
#         })

#     @http.route('/pigeon_hole/pigeon_hole/objects/<model("pigeon_hole.pigeon_hole"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pigeon_hole.object', {
#             'object': obj
#         })