#!/usr/bin/env python3
"""
MRT Api
"""

from flask import Flask, jsonify
from flask_socketio import SocketIO

app = Flask('__name__')

socketio = SocketIO(app)

@app.route('/')
def home():
    return jsonify({"name": "Menofia Racing Team"})

if __name__ == '__main__':
    socketio.run(app, debug=True)
