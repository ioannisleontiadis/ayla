from flask import Flask
from . import db, home, overview

def create_app(test_config=None):
    app = Flask(__name__)

    app.teardown_appcontext(db.close_db)

    app.register_blueprint(home.bp)
    app.register_blueprint(overview.bp)

    return app
