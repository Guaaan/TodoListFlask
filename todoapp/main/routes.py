from flask import Blueprint, render_template, url_for, redirect, request
from bson.objectid import ObjectId

from todoapp.extensions import mongo

main = Blueprint('main', __name__)

# todos = mongo.db.todos

@main.route('/')
def index():
    todos_collection = mongo.db.todos
    todos = todos_collection.find()
    return render_template('index.html', todos=todos)

@main.route('/add_todo', methods=['POST'])
def add_todo():
    todos_collection = mongo.db.todos
    todo_item = request.form.get('add-todo')
    todos_collection.insert_one({'todo': todo_item, 'completed': False})
    return redirect(url_for('main.index'))

@main.route('/complete/<oid>')
def complete_todo(oid):
    todos_collection = mongo.db.todos
    todo_item = todos_collection.replace_one({'_id': ObjectId(oid)})
    todo_item['completed'] = True
    todos_collection.save(todo_item)
    return redirect(url_for('main.index'))

