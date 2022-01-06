from datetime import datetime
from QuenchMarks import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    reviews = db.relationship('Review', backref='user', lazy=True)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username {self.username}"


class Bottle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    brand = db.Column(db.String(64), nullable=False)
    material = db.Column(db.String(64), nullable=False)
    volume = db.Column(db.Integer)
    reviews = db.relationship('Review', backref='bottle', lazy=True)


class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    published = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    bottle_id = db.Column(db.Integer, db.ForeignKey("bottle.id"), nullable=False)
    author = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
