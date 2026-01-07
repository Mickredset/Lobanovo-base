from flask import Flask
from flask_socketio import SocketIO
from .models import db
from .routes import register_routes

socketio = SocketIO()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    socketio.init_app(app, async_mode='gevent')

    register_routes(app)

    with app.app_context():
        db.create_all()

    return app
