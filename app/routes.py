from app import app, db
from flask import render_template, request, redirect
from app.models import User, Task

@app.route('/<name>')
def index(name):
    return f"{name} loves python"

@app.route('/')
def home():
    user = User.query.get(1)
    tasks = user.tasks
    return render_template("index.html", title="Home", user=user, tasks=tasks)

# @app.route('/tasks', methods=['POST'])
# def create():
#     user = User.query.get(1)
#     task_title = request.form['title']
#     task_desc = request.form['description']
#     new_task = Task(title=task_title, description=task_desc, user=user)
#     db.session.add(new_task)
#     db.session.commit()
#     return redirect("/")
@app.route('/tasks', methods=['POST'])
def create():
    user = User.query.get(1)
    task_title = request.form['title']
    task_desc = request.form['description']
    new_task = Task(title=task_title, description=task_desc, user=user)
    db.session.add(new_task)
    db.session.commit()
    return redirect("/")

@app.route('/tasks/<int:task_id>', methods=['POST'])
def update(task_id):
    task = Task.query.get(task_id)
    task.done = True
    db.session.commit()
    return redirect("/")
