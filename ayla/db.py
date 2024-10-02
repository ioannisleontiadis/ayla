from os import environ
from psycopg2 import connect
from flask import g

def get_db():
    if 'db' not in g:
        g.db = connect(
                host=environ['PGHOST'],
                database=environ['PGDATABASE'],
                user=environ['PGUSER'],
                password=environ['PGPASSWORD'],
                port=environ['PGPORT'])

    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
