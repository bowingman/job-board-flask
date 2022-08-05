from ntpath import realpath
from sqlalchemy.orm import relationship
from app import db


class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    rate = db.Column(db.String, nullable=False)
    approved = db.Column(db.Boolean, default=False)
    status = db.Column(db.String, default="ready")
    company_scale = db.Column(db.String, nullable=True)
    company_tips = db.Column(db.String, nullable=True)
    created_at = db.Column(db.Date, nullable=True)
    job_info = db.Column(db.String, nullable=True)

    user = relationship("User",  back_populates="jobs")
    applications = relationship("Application", back_populates="application")
