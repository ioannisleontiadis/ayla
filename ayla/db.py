from os import environ
from psycopg2 import connect
from flask import g

def get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
                host=os.environ['PGHOST'],
                database=os.environ['PGDATABASE'],
                user=os.environ['PGUSER'],
                password=os.environ['PGPASSWORD']
        )

    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
