from flask import Flask, jsonify
from flask_socketio import SocketIO
from dotenv import load_dotenv
from os import getenv
from flask_cors import CORS

load_dotenv()


def create_app():
    app = Flask('__name__')
    app.config['SECRET_KEY'] = getenv("SECRET_KEY")
    socketio = SocketIO(app, cors_allowed_origins="*")
    CORS(app, resources={r"/*": {"origins": "*"}})

    return app, socketio
