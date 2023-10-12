from odoo import models, fields, api
from datetime import datetime, timedelta

class Offer(models.Model):
    _name="estate.property.offer"
    _description="Offers of the buyers"

    price = fields.Float()
    status = fields.Selection(
        string='Status',
        selection=[('accepted','Accepted'),('refused','Refused')],
        copy=False
    )
    partner_id = fields.Many2one("res.partner", string="Buyer", required=True)
    property_id = fields.Many2one("estate.property", string="Property", required=True)
    validity = fields.Integer(default=7, string="Validity (days)")
    date_deadline = fields.Date(compute="_compute_deadline", inverse="_inverse_deadline")

        #COMPUTE METHODS

    @api.depends('validity')
    def _compute_deadline(self):   
        for record in self:
            record.date_deadline = datetime.today().date() + timedelta(days=record.validity)

    def _inverse_deadline(self):   
        for record in self:
            # if(record.offer_ids):
            #     offers = record.offer_ids.mapped('price')
            #     var_best_offer = 0
            #     for price in offers:
            #         if price > var_best_offer: var_best_offer = price

            #     record.best_offer = var_best_offer
            # else:
            #     record.best_offer = 0
            # record.best_offer = max(record.offer_ids.mapped('price'), default=0)
            record.validity = (record.date_deadline - datetime.today().date()).days
