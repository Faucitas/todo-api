from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from app.tasks.models import Task, TaskSchema

bp = Blueprint('tasks', __name__, url_prefix='/tasks')


@bp.route('', methods=['GET'])
def index():
    tasks = Task.get_all()
    return jsonify(TaskSchema(many=True).dump(tasks)), 200


@bp.route('', methods=['POST'])
def create():
    schema = TaskSchema()

    try:
        result = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_task = Task.create(**result)
    return jsonify(schema.dump(new_task)), 201


@bp.route('/<int:task_id>', methods=['GET'])
def show(task_id: int):
    task = Task.get(id=task_id)
    return jsonify(TaskSchema().dump(task)), 200


@bp.route('/<int:task_id>', methods=['PUT'])
def update(task_id: int):
    schema = TaskSchema()

    try:
        result = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    task = Task.get(task_id)
    task.update(**result)

    return jsonify(TaskSchema().dump(task)), 200


@bp.route('<int:task_id>', methods=['DELETE'])
def delete(task_id: int):
    task = Task.get(task_id)
    task.delete()
    return jsonify({"message": f"Deleted Task"}), 200
