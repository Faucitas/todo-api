from flask import Blueprint, jsonify, abort, request
from marshmallow import ValidationError
from app.tasks.models import Task, TaskSchema

bp = Blueprint('tasks', __name__, url_prefix='/tasks')

@bp.route('', methods=['GET'])
def index():
    tasks = Task.get_all()
    result = TaskSchema(many=True).dump(tasks)
    return jsonify(result), 200

