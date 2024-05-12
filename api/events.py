from .config import socketio
from . import views


@socketio.on('connect', namespace="/")
def handle_connect():
    print('Client connected')
    socketio.emit('message', 'Hello from Flask')


def update_voltage(voltage):
    socketio.emit('voltage', {'voltage': voltage})
