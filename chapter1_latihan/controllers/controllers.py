# -*- coding: utf-8 -*-
from odoo import http

# class Latihan1(http.Controller):
#     @http.route('/latihan1/latihan1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/latihan1/latihan1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('latihan1.listing', {
#             'root': '/latihan1/latihan1',
#             'objects': http.request.env['latihan1.latihan1'].search([]),
#         })

#     @http.route('/latihan1/latihan1/objects/<model("latihan1.latihan1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('latihan1.object', {
#             'object': obj
#         })