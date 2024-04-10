from typing import List, Tuple
from odoo import fields, models, api

from ..util import geo_utils

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
    ) -> List[Tuple["ResPartner", float]]:
        search_lookup = []
        if gender:
            search_lookup.append(("gender", "=", gender ))
        partners = self.env["res.partner"].search(search_lookup)

        closest_partners = []
        for partner in partners:
            distance = geo_utils.calculate_distance(
                partner.x_coordinate,
                partner.y_coordinate,
                x,
                y
            )
            if distance <= max_distance:
                closest_partners.append((partner, distance))
        return closest_partners
  