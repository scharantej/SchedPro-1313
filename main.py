
# main.py

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    name = request.form['name']
    description = request.form['description']
    start_time = datetime.strptime(request.form['start_time'], '%Y-%m-%d %H:%M')
    end_time = datetime.strptime(request.form['end_time'], '%Y-%m-%d %H:%M')
    tasks.append({'name': name, 'description': description, 'start_time': start_time, 'end_time': end_time})
    return redirect(url_for('index'))

@app.route('/generate_schedule')
def generate_schedule():
    return render_template('schedule.html', tasks=tasks)

@app.route('/edit_task/<int:index>', methods=['POST'])
def edit_task(index):
    tasks[index]['name'] = request.form['name']
    tasks[index]['description'] = request.form['description']
    tasks[index]['start_time'] = datetime.strptime(request.form['start_time'], '%Y-%m-%d %H:%M')
    tasks[index]['end_time'] = datetime.strptime(request.form['end_time'], '%Y-%m-%d %H:%M')
    return redirect(url_for('index'))

@app.route('/delete_task/<int:index>')
def delete_task(index):
    tasks.pop(index)
    return redirect(url_for('index'))

@app.route('/clear_schedule')
def clear_schedule():
    tasks.clear()
    return redirect(url_for('index'))

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == '__main__':
    app.run(debug=True)
