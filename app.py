from crypt import methods
from flask import Flask, request, Response
from typing import List, Dict

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

if __name__ == '__main__':
    app.run()