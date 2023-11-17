from itertools import groupby
from datetime import datetime, timedelta
from odoo.exceptions import UserError

from odoo import fields, models, api
import logging

_logger = logging.getLogger(__name__)

class PigeonHole(models.Model):
    _name = 'pigeon.hole'
    _desctiption = 'Pigeon Hole Master'
    _inherit = ['mail.thread']

    name = fields.Char(string="Pigeon Hole", required=True, index=True, size=20, help="Gate name")
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
    code = fields.Char(string="Code", required=True, index=True, size=5, help="Gate Code")
    color = fields.Char(string='Color Code', size=8)
    desc = fields.Char(string='desc')
    active = fields.Boolean(string='Active', default=True, track_visibility='always')
    task_line = fields.One2many('task.ph.line', 'ph_id', string='Order Lines', copy=True)
    booking_date = fields.Date(string='Booking Date', copy=False,
                               help="Manually set the expiration date of your quotation (offer), or it will set the date automatically based on the template if online quotation is installed.")
    state = fields.Selection([
        ('draft', 'Free'),
        ('book', 'Booked')], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange',
        default='draft')
    _sql_constraints = [
        ('pigeon_uniq', 'unique(code, company_id)', 'The name and Code Pigeon Hole must be unique!'),
    ]

class Picking(models.Model):
    _inherit = 'stock.picking'

    task_ph_id = fields.Many2one('task.ph.line', string = 'task PH')
    ph_id = fields.Many2one('pigeon.hole', string='Pigeon Hole', related='task_ph_id.ph_id')

class PigeonHoleTask(models.Model):
    _name = 'task.ph.line'
    _desctiption = 'Pigeon Hole Task Lines'
    _inherit = ['mail.thread']

    name = fields.Char(string="Pigeon Hole", required=True, index=True, size=50, help="Gate name")
    ph_id = fields.Many2one('pigeon.hole', string='Gate Pigeon Hole')
    picking_id = fields.Many2one('stock.picking', string='DO/Return')
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.user.company_id)
    user_id = fields.Many2one('res.users', string='Responsible', index=True, track_visibility='onchange',
                              default=lambda self: self.env.user)
    po_transport_id = fields.Integer(string='PO Transport', index=True, track_visibility='onchange')
    do_line = fields.One2many('task.do.ph.line', 'task_id', string='Order Lines', copy=True)
    scheduling_id = fields.Integer(string='Scheduling', index=True, track_visibility='onchange')
    color = fields.Char(string='Color Code', size=8)
    start_date = fields.Date(string='Start Date', copy=False, required=True,
                             help="Manually set the expiration date of your quotation (offer), or it will set the date automatically based on the template if online quotation is installed.")
    finish_date = fields.Date(string='Finish Date', copy=False, required=True,
                              help="Manually set the expiration date of your quotation (offer), or it will set the date automatically based on the template if online quotation is installed.")
    active = fields.Boolean(string='Active', default=True, track_visibility='always')
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('confirm', 'Confirmed'),
        ('done', 'Delivery')
    ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

    @api.multi
    def button_cancel(self):
        return True

    @api.multi
    def button_confirm(self):
        return True

    @api.multi
    def button_shipping(self):
        return True

    @api.multi
    def button_reschedule(self):
        return True

    @api.multi
    def button_add_document(self):
        return True

class TaskDOPH(models.Model):
    _name = 'task.do.ph.line'
    _desctiption = 'Delivery Order Pigeon Hole Lines'

    name = fields.Char(string="No. Doc", required=True)
    customer = fields.Char(string="Receive")
    destination = fields.Char(string="Address")
    task_id = fields.Many2one('task.ph.line', string='Pigeon Hole Task')
    picking_id = fields.Many2one('stock.picking', string='Delivery/Receive Order')
    partner_id = fields.Many2one('res.partner', string='Partner')
    volume = fields.Float(string='Volume')
    weight = fields.Float(string='Weight')
    target_volume = fields.Float(string='Target Volume')
    target_weight = fields.Float(string='target Weight')
    state = fields.Selection(related='task_id.state', string='Status', readonly=True, copy=False, index=True, track_visibility='onchange')


