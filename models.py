# models.py
from flask_login import UserMixin
from app import db
import datetime

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return value.strftime("%Y-%m-%d")+" "+ value.strftime("%H:%M:%S")

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    code = db.Column(db.Integer, nullable=False)
    subcode = db.Column(db.Integer)
    value  = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
            'id' : self.id,
            'code' : self.code,
            'subcode' : self.subcode,
            'value' : self.value,
            'timestamp' : dump_datetime(self.timestamp)
       }

    @classmethod
    def delete_expired_logs(self, expiration_days = 1):
        if expiration_days != -1:
            limit = datetime.datetime.now() - datetime.timedelta(days=expiration_days)
            self.query.filter(self.timestamp <= limit).delete()
            db.session.commit()

class LogJobs(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    program = db.Column(db.Integer, nullable=False)
    product = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)
    time = db.Column(db.Time(), default=0)
    timestamp = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    
    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
            'id' : self.id,
            'program' : self.program,
            'product' : self.product,
            'status' : self.status,
            'time' : self.time.strftime("%H:%M"),
            'timestamp' : dump_datetime(self.timestamp),
       }
