from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, SubmitField, TelField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from core.models import User
import re


class LoginForm(FlaskForm):
	"""Form for login user"""
	username    = StringField(   "Username",    validators = [ DataRequired(), Length( 3, 32 ) ] )
	password    = PasswordField( "Password",    validators = [ DataRequired(), Length( 8, 32 ) ] )
	submit      = SubmitField(   "Submit" )


class RegisterForm(FlaskForm):
	"""Form for register user"""
	name      = StringField(   "Name",         validators = [ DataRequired(), Length( 3, 32 ) ] )
	username  = StringField(   "Login",        validators = [ DataRequired(), Length( 3, 32 ) ] )
	email     = EmailField(    "Email",        validators = [ DataRequired(), Email(), Length( 6, 64 ) ] )
	phone     = TelField(      "Phone",        validators = [ Length( 11, 11 ) ] )
	sex       = RadioField(    "Your sex",     choices    = [ ( "M", "Male" ), ( "F", "Female" ), ( "N", "None" ) ], default = "N")
	password  = PasswordField( "Password",     validators = [ DataRequired(), Length( 8, 32 ) ] )
	password2 = PasswordField( "Password too", validators = [ DataRequired(), EqualTo( "password" ) ] )
	submit    = SubmitField(   "Submit" )

	def validate_username( self, username ):
		user = User.query.filter_by( username = username.data ).first()

		if user is not None:
			raise ValidationError( "Please use a different login" )

		if re.search( '\W', username.data ):
			raise ValidationError( "Use only A-Z, a-z, 0-9 and _" )

	def validate_email( self, email ):
		user = User.query.filter_by( email = email.data ).first()
		if user is not None:
			raise ValidationError( "Please use a different email" )

	def validate_password( self, password ):
		if re.search( "[a-z]", password.data ) is None:
			raise ValidationError( "Use letter in password" )

		if re.search( "[A-Z]", password.data ) is None:
			raise ValidationError( "Use capital in password" )

		if re.search( "[0-9]", password.data ) is None:
			raise ValidationError( "Use number in password" )
