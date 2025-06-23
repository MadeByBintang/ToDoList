from flask import Flask, render_template, request, redirect
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Koneksi ke PostgreSQL dari .env
conn = psycopg2.connect(
    host=os.environ.get("DB_HOST"),
    database=os.environ.get("DB_NAME"),
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD")
)
cur = conn.cursor()

# Buat tabel jika belum ada
cur.execute("""
    CREATE TABLE IF NOT EXISTS todos (
        id SERIAL PRIMARY KEY,
        task TEXT NOT NULL,
        completed BOOLEAN DEFAULT FALSE
    );
""")
conn.commit()

@app.route('/')
def index():
    todo_to_edit = None
    edit_id = request.args.get('edit')
    if edit_id:
        cur.execute("SELECT * FROM todos WHERE id = %s", (edit_id,))
        todo_to_edit = cur.fetchone()

    cur.execute("SELECT id, task, completed FROM todos;")
    todos = cur.fetchall()
    return render_template('index.html', todos=todos, todo_to_edit=todo_to_edit)

@app.route('/add', methods=['POST'])
def add():
    task = request.form['task']
    cur.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
    conn.commit()
    return redirect('/')

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    new_task = request.form['task']
    cur.execute("UPDATE todos SET task = %s WHERE id = %s", (new_task, id))
    conn.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    cur.execute("DELETE FROM todos WHERE id = %s", (id,))
    conn.commit()
    return redirect('/')

@app.route('/complete/<int:id>')
def complete(id):
    cur.execute("SELECT completed FROM todos WHERE id = %s", (id,))
    result = cur.fetchone()
    if result:
        cur.execute("UPDATE todos SET completed = %s WHERE id = %s", (not result[0], id))
        conn.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
