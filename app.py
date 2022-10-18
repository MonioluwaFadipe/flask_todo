from crypt import methods
from flask import Flask, request, Response
from typing import List, Dict
from utils import parse_todo_request

app = Flask(__name__)

todos: List[Dict] = []
total_todos = 0

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/todos', methods=['POST'])
def new_todo():
    request_data = request.get_json()
    todo = parse_todo_request(request_data)
    if None in todo.values():
        response: Response = Response(
            "Invalid request",
            status=400,
            minetype = 'application/json'
        )

if __name__ == '__main__':
    app.run()