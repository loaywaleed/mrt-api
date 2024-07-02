from .config import socketio
from . import views
from .config import db
from .models import SensorReadings


@socketio.on('connect', namespace="/")
def handle_connect():
    print('Client connected')
    socketio.emit('message', 'Hello from Flask')


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


def update_speed_rpm(speed):
    rpm = speed * 10
    socketio.emit('speed', {
        'speed': speed,
        'rpm': rpm
    })


def update_blinkers_temperature(data):
    socketio.emit('blinkers', {
        'blinkers': int(data.get('blinkers')),
    })
    socketio.emit('battery_temperature', {
        'temperature': int(data.get('temperature')),
    })
