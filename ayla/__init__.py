from flask import Flask
from . import db, home

def create_app(test_config=None):
    app = Flask(__name__)

    app.teardown_appcontext(db.close_db)

    app.register_blueprint(home.bp)

    return app
