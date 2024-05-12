#!/usr/bin/env python3
"""
MRT Api
"""

from flask import Flask, jsonify
from flask_socketio import SocketIO
from dotenv import load_dotenv
from os import getenv
from flask_cors import CORS


# Flask Config
load_dotenv()

app = Flask('__name__')
app.config['SECRET_KEY'] = getenv("SECRET_KEY")
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app, resources={r"/*": {"origins": "*"}})


@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit('message', 'Hello from Flask')


@app.route("/", strict_slashes=False, methods=["GET"])
def home():
    return "MRT"


# @app.route("/voltage", strict_slashes=False, methods=["GET"])
# def voltage():
#     socketio.emit('my_event', {'data': 'Some data'}, namespace='/s')
#     return jsonify({"data": "12 V"})


if __name__ == '__main__':
    socketio.run(app, debug=True)
