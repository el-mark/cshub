import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '37a05ef5242d150aa1bb6088332db0db'
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data', 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager(app)
login_manager.login_view = 'login' #when trying to access a page that requires login in, this will redirect you to the login page
login_manager.login_message_category='info' #makes flash message looks nicer

from app import views
from app.models import *

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)