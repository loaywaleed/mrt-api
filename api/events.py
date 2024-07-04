from .config import socketio
from . import views
from .config import db
from .models import SensorReadings


@socketio.on('connect', namespace="/")
def handle_connect():
    print('Client connected')
    socketio.emit('message', 'Connected')


def update_voltage_range_current(data):
    voltage = data.get('voltage')
    current = data.get('current')
    range_available = data.get('range')
    socketio.emit('vi_range', {
        'voltage': voltage,
        'current': current,
        'range': range_available,
    })
    readings = SensorReadings(
        voltage=voltage, current=current, range_available=range_available)
    db.session.add(readings)
    db.session.commit()


def update_speed_rpm_distance(data):
    speed = int(data.get('speed'))
    rpm = int(data.get('rpm'))
    distance = int(data.get('distance'))
    socketio.emit('speed', {
        'speed': speed,
        'rpm': rpm,
        'distance': distance
    })


def update_blinkers_temperature(data):
    socketio.emit('blinkers', {
        'blinkers': int(data.get('blinkers')),
    })
    socketio.emit('battery_temperature', {
        'temperature': int(data.get('temperature')),
    })


def update_gps(data):
    gps_lat = data.get('gps_lat')
    gps_long = data.get('gps_long')
    gps_data = SensorReadings(gps_lat=gps_lat, gps_long=gps_long)
    db.add(gps_data)
    db.commit()
