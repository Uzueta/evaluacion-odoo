from odoo import models, fields

class Tag(models.Model):
    _name="estate.property.tag"
    _description="Tags de propiedades"

    name = fields.Char(required=True, string="Tag")