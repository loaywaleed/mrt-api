#!/usr/bin/env python3
"""
MRT Api
"""

from flask import jsonify
from api.config import create_app
from flask_socketio import emit

app, socketio = create_app()


@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit('message', 'Hello from Flask')


@app.route("/", strict_slashes=False, methods=["GET"])
def home():
    return "MRT"


if __name__ == '__main__':
    socketio.run(app, debug=True)
