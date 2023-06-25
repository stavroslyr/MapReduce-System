from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(80), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(120), nullable=False)

class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(80), nullable=False)

def init_app(app):
    db.init_app(app)