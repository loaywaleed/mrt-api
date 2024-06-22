from .config import socketio
from . import views


@socketio.on('connect', namespace="/")
def handle_connect():
    print('Client connected')
    socketio.emit('message', 'Hello from Flask')


def update_voltage_range_current(data):
    socketio.emit('vi_range', {
        'voltage': data.get('voltage'),
        'current': data.get('current')
        })
