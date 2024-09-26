from flask import Blueprint, redirect, render_template, url_for, request, g
from ayla.db import get_db

bp = Blueprint('home', __name__)

@bp.route('/', methods=['GET'])
def redirect_to_home():
    return redirect(url_for('home.get_home'))

@bp.route('/home', methods=['GET'])
def get_home():
    per_semester_query = """
        SELECT 
            semester,
            FLOOR(COUNT(CASE WHEN grade IS NOT NULL THEN 1 END) * 100.0 / COUNT(*)) AS progress,
            printf('%.2f', SUM(CASE WHEN grade IS NOT NULL THEN grade * coeff ELSE 0 END) / SUM(CASE WHEN grade IS NOT NULL THEN coeff ELSE 0 END)) AS average,
            COUNT(CASE WHEN grade IS NULL THEN 1 END) AS remaining,
            COUNT(CASE WHEN lab = '1' THEN 1 END) AS lab
        FROM 
            course
        GROUP BY 
            semester
        ORDER BY 
            semester;"""
    cur = get_db().cursor()
    semester_stats = cur.execute(per_semester_query).fetchall() or None
    cur.close();
    return render_template('home/home.html', stats=semester_stats)

