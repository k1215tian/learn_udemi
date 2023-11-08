# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
     _name = 'res.partner'
     _inherit = 'res.partner'

     npwp = fields.Char(string='NPWP')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
