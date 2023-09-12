#
# ADMIN MODULE
# ============
# All admin subsystem
#

from flask import Blueprint
from flask_admin import Admin

admin_panel = Blueprint('admin_panel', __name__, url_prefix = "/admin_panel/",
						static_folder = "static", template_folder = "templates")

admin = Admin(admin_panel, template_mode = 'bootstrap3')

from admin_panel import routes
