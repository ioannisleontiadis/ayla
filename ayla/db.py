import os
import psycopg2
from flask import current_app, g

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

def init_app(app):
    app.teardown_appcontext(close_db)

def get_db():
    console.log("get_db()")
    console.log(g)
    if 'db' not in g:
        g.db = psycopg2.connect(
                host=os.environ['PGHOST'],
                database=os.environ['PGDATABASE'],
                user=os.environ['PGUSER'],
                password=os.environ['PGPASSWORD']
        )

    return g.db

def close_db(e=None):
    console.log("closing db")
    db = g.pop('db', None)
    console.log(db)
    if db is not None:
        db.close()
