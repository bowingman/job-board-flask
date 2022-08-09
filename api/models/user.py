from sqlalchemy.orm import relationship
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    password = db.Column(db.String)
    role = db.Column(db.String(20), default="freelancer")
    title = db.Column(db.String, nullable=True)
    description = db.Column(db.String, nullable=True)
    rate = db.Column(db.Integer, default=0)
    approved = db.Column(db.Boolean, default=False)

    jobs = relationship('Job', back_populates="user", lazy=True)
    applications = relationship('Application', back_populates="user")
