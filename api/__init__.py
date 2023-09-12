#
# API MODULE
# ==========
# API
# API pages
# API docs
# API security
#

from flask import Blueprint

api = Blueprint( "api", __name__, url_prefix = "/api/",
				 static_folder = "static", template_folder = "templates")

from api import routes
