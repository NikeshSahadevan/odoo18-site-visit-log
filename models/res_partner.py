from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    site_visit_ids = fields.One2many(
        'site.visit',
        'partner_id',
        string='Site Visits'
    )
    site_visit_count = fields.Integer(
        string='Site Visits Count',
        compute='_compute_site_visit_count'
    )

    def _compute_site_visit_count(self):
        for partner in self:
            partner.site_visit_count = len(partner.site_visit_ids)

    def action_view_site_visits(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Site Visits',
            'res_model': 'site.visit',
            'view_mode': 'list,kanban,calendar,form',
            'domain': [('partner_id', '=', self.id)],
            'context': {'default_partner_id': self.id},
        }