from typing import List, Dict, NoReturn
from datetime import datetime
import uuid

def parse_todo_request(request: Dict) -> Dict:
    #parse request ftom the client and return data in a dict
    cleaned_request =  {
        'id': str(uuid.uuid4()),
        'title': request.get['title'],
        'description': request.get['description'],
        'due_date': request.get['due_date'],
        'completed': request.get['completed'],
        'created_at': datetime.now()
    }

    return cleaned_request
