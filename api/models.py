from .config import db
from datetime import datetime


class SensorReadings(db.Model):
    __tablename__ = "sensors"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.now().date())
    time = db.Column(db.Time, default=datetime.now().time())
    soc = db.Column(db.Integer)  # 0 to 100 check implemented in table manually
    speed = db.Column(db.Integer)
    rpm = db.Column(db.Integer)
    distance_travelled = db.Column(db.Integer)  # cumulative
    range_available = db.Column(db.Integer)
    current = db.Column(db.Float)
    voltage = db.Column(db.Float)
    gps_lat = db.Column(db.Float)
    gps_long = db.Column(db.Float)
    temperature = db.Column(db.Integer)


class VoltageCurrentRange(db.Model):
    __tablename__ = "voltage_current_range"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.now().date())
    time = db.Column(db.Time, default=datetime.now().time())
    range_available = db.Column(db.Integer)
    current = db.Column(db.Float)
    voltage = db.Column(db.Float)