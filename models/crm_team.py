# models/crm_team.py
from odoo import models, fields

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.company.currency_id)
    annual_revenue_target = fields.Monetary(string='Meta de Facturación Anual', currency_field='currency_id')
