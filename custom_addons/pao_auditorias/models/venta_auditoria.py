from odoo import models, fields

class VentaAuditoria(models.Model):
    _inherit="sale.order.line"

    auditoria = fields.Many2one('pao.auditorias', required=True, string="Auditoría", domain="[('cliente', '=', parent.partner_id)]")