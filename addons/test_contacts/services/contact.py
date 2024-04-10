# Copyright 2020 Open Source intgerators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
import json

from typing import Optional
from odoo.addons.component.core import Component
from odoo import http
from odoo.addons.base_rest import restapi
import logging
import re

_logger = logging.getLogger(__name__)
class Account(Component):

    _inherit = "base.rest.service"
    _name = "contact.service"
    _usage = "contact"
    _collection = "ccu.connector.rest.public.services"
    _cors = "*"
    _description =  """
                    Contact Queries
                    ===============
                    Endpoints available:
                    * ``GET /restapi/public/contact/close_contact``: get close contacts sorted
                    """

    @restapi.method(
        [(["/close_contact/",], "GET")],
        input_param=restapi.CerberusValidator({
            "x_coordinates": {"type": "string", "required": True},
            "y_coordinates": {"type": "string", "required": True},
            "max_distance": {"type": "string", "required": True},
            "gender": {"type": "string", "allowed": ["male", "female", "other"]},
        }),
        auth="public",
    )
    def close_contact(self, x_coordinates: str, y_coordinates: str, max_distance: str, gender: Optional[str]=None):
        response_temple = {
            "success": True,
            "error": "",
            "data": []
        }
        try:
            x_coordinates = float(x_coordinates)
            y_coordinates = float(y_coordinates)
            max_distance = float(max_distance)
        except ValueError as e:
            response_temple.update({
                "success": False,
                "error": e
            })
            return http.Response(json.dumps(response_temple), status=400)
        
        partners = self.env["res.partner"].search_closes_partners(
            x_coordinates, y_coordinates, max_distance, gender
        )  

        response_temple.update(
            {
                "data": [
                    {"name": partner.name } 
                    for partner in partners
                ]
            }
        )

        return response_temple