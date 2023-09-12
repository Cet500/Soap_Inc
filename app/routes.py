from flask import redirect, render_template, send_from_directory, request, url_for
from flask_login import current_user, login_user, logout_user
from app import app, db
from app.models import User, Soap
from app.forms import LoginForm, RegisterForm
from datetime import datetime


#    MAIN ROUTES FILE
# ======================
#  * main
#  * tech
#  * admin
#  * login
#  * API
#  * error
#  * tests


# ---------------------- Main pages ---------------------- #


@app.route('/')
@app.route('/index')
def index():
	return render_template("index.html")


@app.route('/catalog')
def catalog():
	soaps = Soap.query.all()

	return render_template("catalog.html", soaps = soaps )


@app.route('/about')
def about():
	return render_template("about.html")


@app.route('/contacts')
def contacts():
	return render_template("contacts.html")


@app.route('/cart')
def cart():
	return render_template("cart.html")


@app.route('/price_list')
def price_list():
	return render_template("price_list.html")


@app.route('/info_bear')
def info_bear():
	return render_template("info_bear.html")


@app.route('/info_penguin')
def info_penguin():
	return render_template("info_penguin.html")


@app.route('/info_puppy')
def info_puppy():
	return render_template("info_puppy.html")


# ---------------------- Tech pages ---------------------- #


@app.route('/favicon.ico')
# @app.route('/robots.txt')
# @app.route('/sitemap.xml')
def static_from_root():
	return send_from_directory(app.static_folder, request.path[1:])


@app.route('/components')
def components():
	return render_template("components.html")


@app.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.datetime_last = datetime.utcnow()
		db.session.commit()


# ---------------------- Admin pages --------------------- #


@app.route('/admin/')
def admin():
	return render_template("admin/index.html")


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
def logout():
	logout_user()
	return redirect( url_for( "index" ) )


# ----------------------- API pages ---------------------- #


@app.route('/api/')
@app.route('/api/index')
def api_index():
	return render_template( "api/index.html" )


@app.route('/api/to_light')
def api_to_light():
	current_user.theme = "L"
	db.session.commit()
	return '<script>document.location.href = document.referrer</script>'


@app.route('/api/to_dark')
def api_to_dark():
	current_user.theme = "D"
	db.session.commit()
	return '<script>document.location.href = document.referrer</script>'


@app.route('/api/confirm_email')
def confirm_email():
	pass


@app.route('/api/reset_password')
def reset_password():
	pass


# ---------------------- Error pages --------------------- #


@app.errorhandler(404)
def error_404(el):
	return render_template( "error/404.html" ), 404


@app.errorhandler(500)
def error_500(el):
	return render_template( "error/500.html" ), 500


# ---------------------- Tests pages --------------------- #


@app.route('/tests/mail/reset_pass')
def mail_test_reset_pass():
	user = { "name": "User" }
	return render_template("email/reset_password.html", user = user)


@app.route('/tests/mail/confirm_email')
def mail_test_confirm_email():
	user = { "name": "User" }
	return render_template( "email/confirm_email.html", user = user )
