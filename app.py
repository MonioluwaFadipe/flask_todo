from flask import Flask, request, Response
from typing import List, Dict
from utils import parse_todo_request, save_todo, get_todo_by_id, update_a_todo
import json

app = Flask(__name__)

todos_list: List[Dict] = []
total_todos = 0

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/todos', methods=['POST'])
def new_todos():
    global total_todos
    global todos_list
    request_data = request.get_json()
    todo = parse_todo_request(request_data)
    if None in todo.values():
        response: Response = Response(
            "Invalid request",
            status=400,
            mimetype = 'application/json'
        )
        return response
    save_todo(todo, todos_list)
    total_todos += 1
    response: Response = Response(
        json.dumps(todo),
        status=201,
        mimetype='application/json'
    )
    return response

@app.route('/todos', methods=['GET'])
def get_todos():
    global todos_list
    response: Response = Response(
        json.dumps(todos_list, default=vars),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/todos/<todo_id>', methods=['GET'])
def get_todo(todo_id):
    global todos_list
    todo = get_todo_by_id(todo_id, todos_list)
    if todo:
        response: Response = Response(
            json.dumps(todo, default=vars),
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        response: Response = Response(
            "Todo not found",
            status=404,
            mimetype='application/json'
        )
        return response

@app.route('/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    global todos_list
    request_data = request.get_json()
    todo = update_a_todo(todo_id, request_data, todos_list)
    if todo:
        response: Response = Response(
            json.dumps(todo, default=vars),
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        response: Response = Response(
            "Todo not found",
            status=404,
            mimetype='application/json'
        )
        return response
        


if __name__ == '__main__':
    app.run()