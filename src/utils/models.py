from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AuditHistory(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    actor = db.Column(db.Integer)
    old_value = db.Column(db.JSON)
    new_value = db.Column(db.JSON)
    modified_at = db.Column(db.DateTime, default=datetime.utcnow)
