from sqlalchemy.orm import relationship
from app import db


class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'), nullable=False)
    content = db.Column(db.String, nullable=False)
    rate = db.Column(db.Integer, nullable=False)
    answer = db.Column(db.String, nullable=True)
    answered = db.Column(db.Boolean, default=False)

    user = relationship("User", back_populates="applications", lazy=True)
    job = relationship("Job", back_populates="applications", lazy=True)
