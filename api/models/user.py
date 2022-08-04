from email.policy import default
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    passowrd = db.Column(db.String, nullable=False)
    role = db.Column(db.String(20), default="freelancer")
    title = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    rate = db.Column(db.Integer, default=0)
