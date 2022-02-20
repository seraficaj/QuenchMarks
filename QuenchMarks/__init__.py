import os 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'topsecretlol'

### Database Setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://lzammzcztqqqmx:61dd9079a9c546ff59c75cfc600a0e710d55c5f950f04ea51bc805e5355e297a@ec2-54-225-228-142.compute-1.amazonaws.com:5432/d83k5m2mqm9t9h"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
Migrate(app, db)

### Login Configurations
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = "users.login"

from QuenchMarks.core.views import core
from QuenchMarks.users.views import users
from QuenchMarks.bottles.views import bottles
from QuenchMarks.reviews.views import reviews
from QuenchMarks.error_pages.handlers import error_pages

app.register_blueprint(core)
app.register_blueprint(bottles)
app.register_blueprint(users)
app.register_blueprint(reviews)