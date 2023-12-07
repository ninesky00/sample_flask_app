from dotenv.main import load_dotenv
import os
from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
load_dotenv()
app.config['MYSQL_HOST'] = os.environ['MYSQL_HOST']
app.config['MYSQL_USER'] = os.environ['MYSQL_USER']
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = os.environ['MYSQL_DB']

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tasks')
    tasks = cur.fetchall()
    cur.close()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_name = request.form['task_name']
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO tasks (task_name) VALUES (%s)', (task_name,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': 'success'})

@app.route('/delete/<int:task_id>', methods=['DELETE'])
def delete(task_id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM tasks WHERE id = %s', (task_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
