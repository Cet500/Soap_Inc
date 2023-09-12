#
# CORE MODULE
# ===========
# Main pages
# DB, ORM and migrate
# Login subsystem
# Technical and temp/test pages
# Error handlers
# Main array of static files
#

from flask import Blueprint

core = Blueprint("core", __name__, static_folder = "static", static_url_path = "/", template_folder = "templates")

from core import routes, models
