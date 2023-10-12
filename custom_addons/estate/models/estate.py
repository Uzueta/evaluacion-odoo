from odoo import models, fields
from datetime import datetime, timedelta

class Estate(models.Model):
    _name="estate.property"
    _description="Modulo de prueba"

    name = fields.Char(required=True, string="Nombre")
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(copy=False, default=datetime.today() + timedelta(days=90) )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string='Garden orientation',
        selection=[('north','North'),('south','South'),('east','East'),('west','West')]
    )
    active =  fields.Boolean(default=True)
    state = fields.Selection( required=True, copy=False, default="new",
        string='State',
        selection=[('new','New'),('offer_received','Offer Received'),('offer_accepted','Offer Accepted'),('sold','Sold'), ('canceled','Canceled')]
    )
    property_type_id = fields.Many2one("estate.property.type", string="Type")

    salesperson_id = fields.Many2one("res.users", string="Sales Person", index=True, default=lambda self: self.env.user)

    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)

    tag_ids = fields.Many2many("estate.property.tag", string="Tags")






