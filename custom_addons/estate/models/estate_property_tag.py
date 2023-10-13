from odoo import models, fields

class Tag(models.Model):
    _name="estate.property.tag"
    _description="Tags de propiedades"
    _order = "name"

    name = fields.Char(required=True, string="Tag")
    color = fields.Integer()

    _sql_constraints = [('check_tag_name', 'unique(name)','The provided tag name already exists.')]