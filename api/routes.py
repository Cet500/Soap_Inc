from flask import render_template
from flask_login import current_user, login_required
from app import db
from api import api


# API ROUTES FILE
# ===============
# api


# ----------------------- API pages ---------------------- #


@api.route('/')
@api.route('/index')
def index():
	return render_template( "api/index.html" )


@api.route('/to_light')
@login_required
def to_light():
	current_user.theme = "L"
	db.session.commit()
	return '<script>document.location.href = document.referrer</script>'


@api.route('/to_dark')
@login_required
def to_dark():
	current_user.theme = "D"
	db.session.commit()
	return '<script>document.location.href = document.referrer</script>'


@api.route('/confirm_email')
def confirm_email():
	# TODO: Внедрить подтверждение эл. почты
	pass


@api.route('/reset_password')
def reset_password():
	# TODO: Сделать сброс пароля
	pass
