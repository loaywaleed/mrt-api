from flask import Flask
from flask_socketio import SocketIO
from dotenv import load_dotenv
from os import getenv
from flask_cors import CORS


socketio = SocketIO(cors_allowed_origins="*")


def create_app():
    load_dotenv()
    app = Flask('__name__')
    app.config['SECRET_KEY'] = getenv("SECRET_KEY")
    CORS(app, resources={r"/*": {"origins": "*"}})

    from .views import views
    app.register_blueprint(views, url_prefix="/api")
    socketio.init_app(app)

    return app
