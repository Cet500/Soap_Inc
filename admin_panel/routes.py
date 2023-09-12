from flask import render_template
from admin_panel import admin_panel


# ADMIN ROUTES FILE
# =================
# admin


# --------------------- Admin pages ---------------------- #


@admin_panel.route('/')
@admin_panel.route('/index')
def admin():
	return render_template("admin_panel/index.html")
