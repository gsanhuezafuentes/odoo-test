import math
from odoo import fields, models, api, exceptions

class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_coordinate = fields.Float('X Coordinate')
    y_coordinate = fields.Float('Y Coordinate')
    gender = fields.Selection(selection=[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender', required=True)

    @api.model
    def search_closes_partners(
        self, x: float, y:float, max_distance:float, gender: str=None
    ):
        search_lookup = []
        if gender:
            search_lookup.append(("gender", "=", gender ))
        partners = self.env["res.partner"].search(search_lookup)

        closest_partners = []
        for partner in partners:
            distance = math.sqrt((partner.x_coordinate - x)**2 + (partner.y_coordinate - y)**2)
            if distance <= max_distance:
                closest_partners.append(partner)
        return closest_partners
  