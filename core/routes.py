from flask import redirect, render_template, send_from_directory, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from core import core
from core.models import User, Soap
from core.forms import LoginForm, RegisterForm
from datetime import datetime


# CORE ROUTES FILE
# ================
# main
# tech
# login
# error
# tests


# ---------------------- Main pages ---------------------- #


@core.route('/')
@core.route('/index')
def index():
	return render_template("core/index.html")


@core.route('/catalog')
def catalog():
	soaps = Soap.query.all()

	return render_template("core/catalog.html", soaps = soaps )


@core.route('/about')
def about():
	return render_template("core/about.html")


@core.route('/contacts')
def contacts():
	return render_template("core/contacts.html")


@core.route('/cart')
def cart():
	return render_template("core/cart.html")


@core.route('/price_list')
def price_list():
	return render_template("core/price_list.html")


@core.route('/info_bear')
def info_bear():
	return render_template("core/info_bear.html")


@core.route('/info_penguin')
def info_penguin():
	return render_template("core/info_penguin.html")


@core.route('/info_puppy')
def info_puppy():
	return render_template("core/info_puppy.html")


# ---------------------- Tech pages ---------------------- #


@core.route('/favicon.ico')
# TODO: когда-нибудь сделать эти файлы
# @core.route('/robots.txt')
# @core.route('/sitemap.xml')
def static_from_root():
	return send_from_directory(core.static_folder, request.path[1:])


@core.route('/components')
@login_required
def components():
	return render_template("core/components.html")


@core.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.datetime_last = datetime.utcnow()
		db.session.commit()


# ---------------------- Login system -------------------- #


@core.route('/login', methods = [ 'GET', 'POST' ])
def login():
	if current_user.is_authenticated:
		return redirect( url_for("core.index") )

	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by( username = form.username.data ).first()

		if user is None or not user.check_password( form.password.data ):
			return redirect( url_for( "core.login" ) )

		login_user( user, True )

		return redirect( url_for( "core.index" ) )

	return render_template("forms/login.html", form = form)


@core.route('/register', methods = [ 'GET', 'POST' ])
def register():
	if current_user.is_authenticated:
		return redirect( url_for("core.index") )

	form = RegisterForm()

	if form.validate_on_submit():
		u = User( name     = form.name.data,      # type: ignore[call-arg]
				  username = form.username.data,  # type: ignore[call-arg]
				  email    = form.email.data,     # type: ignore[call-arg]
				  phone    = form.phone.data,     # type: ignore[call-arg]
				  sex      = form.sex.data )      # type: ignore[call-arg]
		u.set_password( password = form.password.data )
		db.session.add(u)
		db.session.commit()
		return redirect( url_for( "core.login" ) )

	return render_template("forms/register.html", form = form)


@core.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect( url_for( "core.index" ) )


# ---------------------- Error pages --------------------- #
# TODO: Сделать страницы ошибок более информативными


@core.errorhandler(401)
def error_401(el):
	return render_template( "error/401.html" ), 401


@core.errorhandler(404)
def error_404(el):
	return render_template( "error/404.html" ), 404


@core.errorhandler(500)
def error_500(el):
	return render_template( "error/500.html" ), 500


# ---------------------- Tests pages --------------------- #


@core.route('/tests/mail/reset_pass')
@login_required
def mail_test_reset_pass():
	user = { "name": "User" }
	return render_template("email/reset_password.html", user = user)


@core.route('/tests/mail/confirm_email')
@login_required
def mail_test_confirm_email():
	user = { "name": "User" }
	return render_template( "email/confirm_email.html", user = user )
