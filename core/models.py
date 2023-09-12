from app import db, login
from flask_login import UserMixin
from datetime import datetime
from sqlalchemy.dialects.mysql import SMALLINT
from werkzeug.security import generate_password_hash, check_password_hash


# ---------------------- Soap block ---------------------- #


class Soap(db.Model):
    """Soap datatable"""

    id    = db.Column( db.Integer, primary_key = True )
    type  = db.Column( db.String(10), nullable = False )
    title = db.Column( db.String(50), unique = True, nullable = False )
    color = db.Column( db.String(20) )
    aroma = db.Column( db.String(20) )
    image = db.Column( db.String(20) )
    price = db.Column( SMALLINT( unsigned = True ), default = 0, nullable = False )
    datetime_add = db.Column( db.DateTime, default = datetime.utcnow(),
                              index = True, nullable = False )
    datetime_upd = db.Column( db.DateTime, default = datetime.utcnow(),
                              onupdate = datetime.utcnow(), nullable = False )

    def __repr__( self ):
        return f'<soap {self.title}>'


# ---------------------- Users block --------------------- #


class User(UserMixin, db.Model):
    """User datatable"""

    id            = db.Column( db.Integer, primary_key = True )
    username      = db.Column( db.String(32), index = True, unique = True, nullable = False )
    name          = db.Column( db.String(32), nullable = False )
    lastname      = db.Column( db.String(32) )
    patronymic    = db.Column( db.String(32) )
    email         = db.Column( db.String(64), index = True, unique = True, nullable = False )
    pass_hash     = db.Column( db.String(128), nullable = False )
    description   = db.Column( db.String(256) )
    sex           = db.Column( db.String(1), default = 'N' )
    role          = db.Column( db.String(1), default = 'U' )
    theme         = db.Column( db.String(1), default = 'L' )
    phone         = db.Column( db.String(11) )
    datetime_last = db.Column( db.DateTime, index = True, default = datetime.utcnow() )
    datetime_reg  = db.Column( db.DateTime, index = True, default = datetime.utcnow() )
    datetime_upd  = db.Column( db.DateTime, default = datetime.utcnow(), onupdate = datetime.utcnow() )

    def __repr__( self ):
        return f'<user {self.username}>'

    def set_password( self, password ):
        self.pass_hash = generate_password_hash( password )

    def check_password( self, password ):
        return check_password_hash( self.pass_hash, password )


@login.user_loader
def load_user( user_id ):
    return User.query.get( int( user_id ) )
