#!/usr/bin/env python3
"""
MRT app
"""

from flask import jsonify
from api.config import create_app, socketio
from flask_socketio import emit

app = create_app()

if __name__ == '__main__':
    socketio.run(app, debug=True)
