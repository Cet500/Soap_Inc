from flask import Flask
from config import Config

from flask_admin import Admin
from flask_babel import Babel
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# Flask init
app = Flask(__name__)
app.config.from_object(Config)

# Babel init
babel = Babel()
babel.init_app(app)

# DB init
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Login subsystem init
login = LoginManager(app)

# Admin init
admin = Admin(app, template_mode = 'bootstrap3')

from app import routes, models, admin
