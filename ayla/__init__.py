from flask import Flask
from . import db

def create_app(test_config=None):
    app = Flask(__name__)

    app.teardown_appcontext(close_db)

    app.register_blueprint(home.bp)

    return app
