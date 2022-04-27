from flask import Blueprint, jsonify, abort, request
from marshmallow import ValidationError
from app.tasks.models import Task

bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@bp.route('', methods=['GET'])
def index():
    tasks = Task.query.all()
    result = []
    for task in tasks:
        result.append(
            {
                'id': task._id,
                'description': task.description,
                'complete': task.complete,
            }
        )
    return jsonify(result)