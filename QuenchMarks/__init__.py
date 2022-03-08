import os 
from dotenv import load_dotenv
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

### import .env
load_dotenv()

DB_URI = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY");

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY


### Database Setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URI
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