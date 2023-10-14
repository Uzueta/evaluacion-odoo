from odoo import models, fields

class Auditoria(models.Model):
    _name="pao.auditorias"
    _description="Auditorías a líneas de órdenes de venta"

    numero = fields.Char(required=True, string="Número de Auditoría")
    cliente = fields.Many2one("res.partner", required=True)
    pais = fields.Many2one('res.country', string="País de Auditoría", default=lambda self: self.env['res.country'].search([('code', '=', 'MX')], limit=1))
    estado = fields.Many2one('res.country.state', string="Estado de Auditoría", domain="[('country_id', '=', pais)]")
    ciudad = fields.Many2one('res.city', string="Ciudad de Auditoría", domain="[('state_id', '=', estado)]")
    
    _sql_constraints = [('check_numero_auditoria', 'unique(numero)','El número de auditoría ingresado ya existe.')]

    _rec_name = 'numero'