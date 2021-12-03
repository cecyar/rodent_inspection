from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Inspection(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    job_ticket_or_work_order_id = db.Column(db.Integer)
    job_id = db.Column(db.Text)  #job_id = db.Column(db.JSON)
    inspection_type = db.Column(db.Text)
    boro_code = db.Column(db.Integer)
    zip_code = db.Column(db.Integer)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    inspection_date = db.Column(db.DateTime)
    result = db.Column(db.Text)
    #modified_at = db.Column(db.DateTime, default=datetime.utcnow)