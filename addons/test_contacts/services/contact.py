# Copyright 2020 Open Source intgerators
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
from odoo.addons.component.core import Component
from odoo import http
from odoo.addons.base_rest import restapi
import logging
import re
from odoo.exceptions import UserError

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
    def close_contact(self, x_coordinates, y_coordinates, max_distance, gender=None):
        try:
            x_coordinates = float(x_coordinates)
            y_coordinates = float(y_coordinates)
            max_distance = float(max_distance)
        except ValueError:
            raise UserError("Una de las propiedades no es un numero valido")

        partners = self.env["res.partner"].search_closes_partners(
            x_coordinates, y_coordinates, max_distance, gender
        )  

        return {
            "success": True,
            "error": "",
            "data": [
                {"name": partner.name } 
                for partner in partners
            ]
        }