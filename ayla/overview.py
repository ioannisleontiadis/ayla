from flask import Blueprint, g, redirect, render_template, request, url_for
from ayla.db import get_db
import psycopg2.extras

bp = Blueprint('overview', __name__, url_prefix='/overview')

@bp.route('/', methods=['GET'])
def overview():
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
 
    semesters = []
    for index in range(6):
        query = f'SELECT * FROM courses WHERE semester = {index+1};'
        cur.execute(query)
        stats = cur.fetchall()
        semesters.append(stats)
    return render_template('overview/overview.html', semesters=semesters)
