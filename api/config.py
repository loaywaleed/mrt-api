from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import getenv
from flask_cors import CORS


socketio = SocketIO(cors_allowed_origins="*")

#db = SQLAlchemy()


def create_app():
    load_dotenv()
    app = Flask('__name__')
    #app.config['SQLALCHEMY_DATABASE_URI'] = getenv("DATABASE_URI")
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = getenv("SECRET_KEY")
    CORS(app, resources={r"/*": {"origins": "*"}})

    #db.init_app(app)
    socketio.init_app(app)
    from .views import views
    app.register_blueprint(views, url_prefix='/api')
    #from .models import SensorReadings

    #with app.app_context():
     #   db.create_all()

    return app
