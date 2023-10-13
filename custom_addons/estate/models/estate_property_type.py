from odoo import models, fields

class Type(models.Model):
    _name="estate.property.type"
    _description="Tipos de propiedades"
    _order = "sequence, name"

    name = fields.Char(required=True, string="Nombre")
    property_ids = fields.One2many("estate.property", "property_type_id", readonly=True)
    sequence = fields.Integer('Sequence', default=1)

    _sql_constraints = [('check_type_name', 'unique(name)','The provided type name already exists.')]