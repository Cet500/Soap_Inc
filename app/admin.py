from app import app, admin, db
from models import Soap, User
from flask_admin.contrib.sqla import ModelView

# admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Soap, db.session))


