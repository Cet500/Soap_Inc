import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
	# Hardcode values
	TEMPLATES_AUTO_RELOAD = True
	FLASK_ADMIN_SWATCH = 'darkly'

	# Forms config
	CSRF_ENABLED = True
	SECRET_KEY = os.environ.get('SECRET_KEY')

	# DB config
	SQLALCHEMY_DATABASE_URI = os.environ.get('MYSQL')
	SQLALCHEMY_TRACK_MODIFICATIONS = False
