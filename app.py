# Habit Tracker Pro - Flask Application
# A web application for tracking daily habits with interactive dashboard

from flask import Flask, render_template, request, jsonify
import database
import calendar
from sqlite3 import IntegrityError

# Initialize Flask application
app = Flask(__name__)

# Initialize the database
database.init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/habits', methods=['GET'])
def get_habits():
    conn = database.get_db_connection()
    habits = conn.execute('SELECT * FROM habits ORDER BY id ASC').fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in habits])

@app.route('/api/logs/<int:year>/<int:month>', methods=['GET'])
def get_logs(year, month):
    conn = database.get_db_connection()
    date_prefix = f"{year}-{month:02d}%"
    logs = conn.execute("SELECT habit_id, date, completed FROM habit_logs WHERE date LIKE ?", (date_prefix,)).fetchall()
    conn.close()
    return jsonify([dict(ix) for ix in logs])

@app.route('/api/toggle', methods=['POST'])
def toggle_habit():
    data = request.json
    conn = database.get_db_connection()
    existing = conn.execute('SELECT completed FROM habit_logs WHERE habit_id = ? AND date = ?', 
                            (data['habit_id'], data['date'])).fetchone()
    
    if existing:
        new_status = not existing['completed']
        conn.execute('UPDATE habit_logs SET completed = ? WHERE habit_id = ? AND date = ?',
                     (new_status, data['habit_id'], data['date']))
    else:
        new_status = True
        conn.execute('INSERT INTO habit_logs (habit_id, date, completed) VALUES (?, ?, ?)',
                     (data['habit_id'], data['date'], new_status))
    
    conn.commit()
    conn.close()
    return jsonify({"status": "success", "completed": new_status})

@app.route('/api/habits', methods=['POST'])
def create_habit():
    data = request.json or {}
    name = (data.get('name') or '').strip()
    if not name:
        return jsonify({"error": "name required"}), 400

    conn = database.get_db_connection()
    try:
        cur = conn.execute('INSERT INTO habits (name) VALUES (?)', (name,))
        conn.commit()
        habit_id = cur.lastrowid
    except Exception:
        conn.close()
        return jsonify({"error": "duplicate or database error"}), 400
    conn.close()
    return jsonify({"id": habit_id, "name": name}), 201

@app.route('/api/habits/<int:habit_id>', methods=['DELETE'])
def delete_habit(habit_id):
    conn = database.get_db_connection()
    conn.execute('DELETE FROM habit_logs WHERE habit_id = ?', (habit_id,))
    conn.execute('DELETE FROM habits WHERE id = ?', (habit_id,))
    conn.commit()
    conn.close()
    return jsonify({"status": "deleted", "id": habit_id})

@app.route('/api/habits/clear', methods=['POST'])
def clear_habits():
    conn = database.get_db_connection()
    conn.execute('DELETE FROM habit_logs')
    conn.execute('DELETE FROM habits')
    conn.commit()
    conn.close()
    return jsonify({"status": "cleared"})

@app.route('/api/stats/<int:year>/<int:month>', methods=['GET'])
def get_stats(year, month):
    conn = database.get_db_connection()
    logs = conn.execute("SELECT * FROM habit_logs WHERE date LIKE ? AND completed = 1", 
                        (f"{year}-{month:02d}%",)).fetchall()
    habit_count = conn.execute("SELECT COUNT(*) FROM habits").fetchone()[0]
    conn.close()

    days_in_month = calendar.monthrange(year, month)[1]
    stats = {
        "daily": {d: 0 for d in range(1, days_in_month + 1)},
        "weekly": {1: 0, 2: 0, 3: 0, 4: 0, 5: 0},
        "total_completed": len(logs),
        "total_possible": habit_count * days_in_month
    }

    for log in logs:
        day = int(log['date'].split('-')[2])
        stats["daily"][day] += 1
        if day <= 7: stats["weekly"][1] += 1
        elif day <= 14: stats["weekly"][2] += 1
        elif day <= 21: stats["weekly"][3] += 1
        elif day <= 28: stats["weekly"][4] += 1
        else: stats["weekly"][5] += 1

    return jsonify(stats)

if __name__ == '__main__':
    app.run(debug=True, port=5000)