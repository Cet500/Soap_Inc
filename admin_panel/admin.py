from __main__ import app, admin, db
from core.models import Soap, User
from flask import url_for, redirect, request
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user


class MicroBlogModelView(ModelView):
	# Override of basic functions
	def is_accessible(self):
		if current_user.is_authenticated:
			if current_user.role == "A":
				return True
			else:
				return False
		else:
			return False

	def inaccessible_callback(self, name, **kwargs):
		# redirect to login page if user doesn't have access
		return redirect( url_for('login') )


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Soap, db.session))
