#!/usr/bin/env python3

from models.user import User
from models import storage
from flask import (Blueprint, request, make_response, jsonify, abort)
from sqlalchemy.exc import IntegrityError

bp = Blueprint('user', __name__, url_prefix='/api/v1')

@bp.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")

    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = User(**data)
    try:
        instance.save()
    except IntegrityError as e:
        abort(400, description="User with email already exists")
    return make_response(jsonify(instance.to_dict()), 201)

@bp.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    return jsonify(user.to_dict()), 200


@bp.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def put_user(user_id):
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200)
