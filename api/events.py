from .config import socketio
from . import views


@socketio.on('connect', namespace="/")
def handle_connect():
    print('Client connected')
    socketio.emit('message', 'Hello from Flask')


def update_voltage_range_current(data):
    socketio.emit('vi_range', {
        'voltage': data.get('voltage'),
        'current': data.get('current'),
        'range': data.get('range'),
    })


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
