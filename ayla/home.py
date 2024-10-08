from flask import Blueprint, redirect, render_template, url_for, request, g
from ayla.db import get_db
import psycopg2.extras

bp = Blueprint('home', __name__)

@bp.route('/', methods=['GET'])
def get_home():
    per_semester_query = """
        SELECT 
            semester,
            ROUND(COUNT(CASE WHEN grade IS NOT NULL THEN 1 END) * 100.0 / COUNT(*), 2) AS progress,
            ROUND(SUM(CASE WHEN grade IS NOT NULL THEN grade * coeff ELSE 0 END) / SUM(CASE WHEN grade IS NOT NULL THEN coeff ELSE 0 END),2) AS average,
            COUNT(CASE WHEN grade IS NULL THEN 1 END) AS remaining,
            COUNT(CASE WHEN lab_completed IS false THEN 1 END) AS lab
        FROM 
            courses
        GROUP BY 
            semester
        ORDER BY 
            semester;"""
    conn = get_db()
    cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(per_semester_query)
    semester_stats = cur.fetchall()
    return render_template('home/home.html', stats=semester_stats)
