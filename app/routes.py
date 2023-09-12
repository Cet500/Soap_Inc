from flask import redirect, render_template, send_from_directory, request, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app import app, db
from app.models import User, Soap
from app.forms import LoginForm, RegisterForm
from datetime import datetime


#    MAIN ROUTES FILE
# ======================
#  * main
#  * tech
#  * login
#  * API
#  * error
#  * tests


# ---------------------- Main pages ---------------------- #


@app.route('/')
@app.route('/index')
def index():
	return render_template("app/index.html")


@app.route('/catalog')
def catalog():
	soaps = Soap.query.all()

	return render_template("app/catalog.html", soaps = soaps )


@app.route('/about')
def about():
	return render_template("app/about.html")


@app.route('/contacts')
def contacts():
	return render_template("app/contacts.html")


@app.route('/cart')
def cart():
	return render_template("app/cart.html")


@app.route('/price_list')
def price_list():
	return render_template("app/price_list.html")


@app.route('/info_bear')
def info_bear():
	return render_template("app/info_bear.html")


@app.route('/info_penguin')
def info_penguin():
	return render_template("app/info_penguin.html")


@app.route('/info_puppy')
def info_puppy():
	return render_template("app/info_puppy.html")


# ---------------------- Tech pages ---------------------- #


@app.route('/favicon.ico')
# TODO: когда-нибудь сделать эти файлы
# @app.route('/robots.txt')
# @app.route('/sitemap.xml')
def static_from_root():
	return send_from_directory(app.static_folder, request.path[1:])


@app.route('/components')
@login_required
def components():
	return render_template("app/components.html")


@app.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.datetime_last = datetime.utcnow()
		db.session.commit()


# ---------------------- Admin pages --------------------- #


@app.route('/admin/')
@login_required
def admin():
	if current_user.role == "A":
		return render_template("admin/index.html")
	else:
		return redirect( url_for("login") )


# ---------------------- Login system -------------------- #


@app.route('/login', methods = [ 'GET', 'POST' ])
def login():
	if current_user.is_authenticated:
		return redirect( url_for("index") )

	form = LoginForm()

	if form.validate_on_submit():
		user = User.query.filter_by( username = form.username.data ).first()

		if user is None or not user.check_password( form.password.data ):
			return redirect( url_for( "login" ) )

		login_user( user, True )

		return redirect( url_for( "index" ) )

	return render_template("forms/login.html", form = form)


@app.route('/register', methods = [ 'GET', 'POST' ])
def register():
	if current_user.is_authenticated:
		return redirect( url_for("index") )

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
		return redirect( url_for( "login" ) )

	return render_template("forms/register.html", form = form)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect( url_for( "index" ) )


# ----------------------- API pages ---------------------- #


@app.route('/api/')
@app.route('/api/index')
def api_index():
	return render_template( "api/index.html" )


@app.route('/api/to_light')
@login_required
def api_to_light():
	current_user.theme = "L"
	db.session.commit()
	return '<script>document.location.href = document.referrer</script>'


@app.route('/api/to_dark')
@login_required
def api_to_dark():
	current_user.theme = "D"
	db.session.commit()
	return '<script>document.location.href = document.referrer</script>'


@app.route('/api/confirm_email')
def confirm_email():
	# TODO: Внедрить подтверждение эл. почты
	pass


@app.route('/api/reset_password')
def reset_password():
	# TODO: Сделать сброс пароля
	pass


# ---------------------- Error pages --------------------- #
# TODO: Сделать страницы ошибок более информативными


@app.errorhandler(401)
def error_401(el):
	return render_template( "error/401.html" ), 401


@app.errorhandler(404)
def error_404(el):
	return render_template( "error/404.html" ), 404


@app.errorhandler(500)
def error_500(el):
	return render_template( "error/500.html" ), 500


# ---------------------- Tests pages --------------------- #


@app.route('/tests/mail/reset_pass')
@login_required
def mail_test_reset_pass():
	user = { "name": "User" }
	return render_template("email/reset_password.html", user = user)


@app.route('/tests/mail/confirm_email')
@login_required
def mail_test_confirm_email():
	user = { "name": "User" }
	return render_template( "email/confirm_email.html", user = user )
