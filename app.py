from flask import Flask
from config import Config

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

# Blueprints init
from admin_panel import admin_panel
from api import api
from core import core

app.register_blueprint( admin_panel )
app.register_blueprint( api )
app.register_blueprint( core )
