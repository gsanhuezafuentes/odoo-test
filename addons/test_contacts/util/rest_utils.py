from typing import Dict, List, Union
import json

from odoo import http

def api_response(response: Union[List, Dict], status: int):
    return http.Response(json.dumps(response), status=status)