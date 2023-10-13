from odoo import models, fields, api, exceptions
from odoo.tools.float_utils import float_compare
from datetime import datetime, timedelta

import logging

_logger = logging.getLogger(__name__)

class Estate(models.Model):
    _name="estate.property"
    _description="Real Estate's properties"
    _order = "id desc"

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

    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")

    total_area = fields.Integer(compute="_compute_area", string="Total Area (sqm)")

    best_offer = fields.Float(compute="_compute_best_offer")


    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price > 0)',
         'The expected price of a property must be greater than 0'),
         ('check_selling_price', 'CHECK(selling_price > 0)',
         'The selling price of a property must be greater than 0'),
    ]


    #COMPUTE METHODS (INCLINARSRE MAS POR COMPUTE METHODS)

    @api.depends('living_area', 'garden_area')
    def _compute_area(self):   
        for record in self:
            record.total_area = record.living_area + record.garden_area

    @api.depends('offer_ids.price')
    def _compute_best_offer(self):   
        for record in self:
            # if(record.offer_ids):
            #     offers = record.offer_ids.mapped('price')
            #     var_best_offer = 0
            #     for price in offers:
            #         if price > var_best_offer: var_best_offer = price

            #     record.best_offer = var_best_offer
            # else:
            #     record.best_offer = 0
            record.best_offer = max(record.offer_ids.mapped('price'), default=0)


    # ONCHANGE METHODS

    @api.onchange("garden")
    def _onchange_default_garden(self):
        if self.garden:
            self.garden_area=10
            self.garden_orientation='north'
        else:
            self.garden_area=0
            self.garden_orientation=''

    #ACTION

    def action_sold_property(self):
        for record in self:
            if record.state != "canceled":
                record.state = "sold"
            else:
                raise exceptions.UserError("A canceled property can't be sold")
        return True
    
    def action_cancel_property(self):
        for record in self:
            if record.state != "sold":
                record.state = "canceled"
            else:
                raise exceptions.UserError("A sold property can't be canceled")
        return True
    
    #CONSTRAINTS
    
    @api.constrains('expected_price','selling_price')
    def check_prices(self):
        for record in self:
            if record.selling_price > 0 and float_compare(record.selling_price, (record.expected_price * 0.90), precision_digits=2) < 0:
                raise exceptions.ValidationError('The selling price must be at least the 90% of the expected price')









