from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SiteVisit(models.Model):
    _name = 'site.visit'
    _description = 'Site Visit Log'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'reference desc'

    reference = fields.Char(
        string='Visit Reference',
        required=True,
        copy=False,
        readonly=True,
        default='New'
    )
    name = fields.Char(string='Visit Purpose', required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, tracking=True)
    customer_phone = fields.Char(
        string='Customer Phone',
        related='partner_id.phone',
        readonly=True
    )
    user_id = fields.Many2one(
        'res.users',
        string='Salesperson',
        default=lambda self: self.env.user,
        tracking=True
    )
    visit_date = fields.Date(string='Visit Date', default=fields.Date.context_today, tracking=True)
    notes = fields.Text(string='Notes')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('done', 'Done'),
    ], string='Status', default='draft', tracking=True)
    visit_summary = fields.Char(
        string='Visit Summary',
        compute='_compute_visit_summary',
        store=True
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('reference', 'New') == 'New':
                vals['reference'] = self.env['ir.sequence'].next_by_code('site.visit') or 'New'
        return super().create(vals_list)

    @api.depends('partner_id', 'visit_date')
    def _compute_visit_summary(self):
        for record in self:
            customer = record.partner_id.name or 'Unknown Customer'
            date_str = str(record.visit_date) if record.visit_date else 'No Date'
            record.visit_summary = f"{customer} ({date_str})"

    @api.constrains('visit_date')
    def _check_visit_date(self):
        today = fields.Date.context_today(self)
        for record in self:
            if record.visit_date and record.visit_date > today:
                raise ValidationError("Visit Date cannot be in the future!")

    def action_done(self):
        for record in self:
            record.state = 'done'

    def action_draft(self):
        for record in self:
            record.state = 'draft'