from flask import render_template, url_for
from flask_babel import _, get_locale
from app import app, db
from app.models import Soap


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/catalog')
def catalog():
    return render_template("catalog.html" ) #soaps = soaps


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


@app.route('/components')
def components():
    return render_template("components.html")
