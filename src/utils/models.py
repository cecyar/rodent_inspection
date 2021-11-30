from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Inspection(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    inspection_type = db.Column(db.Text)
    job_ticket_or_work_order_id = db.Column(db.Integer)
    job_id = db.Column(db.JSON)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow)
