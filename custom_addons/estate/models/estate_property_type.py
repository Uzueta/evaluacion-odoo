from odoo import models, fields

class Type(models.Model):
    _name="estate.property.type"
    _description="Tipos de propiedades"

    name = fields.Char(required=True, string="Nombre")