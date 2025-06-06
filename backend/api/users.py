from flask import Blueprint, request, jsonify
from models.users import User
from db import db

user_bp = Blueprint('user', __name__)

@user_bp.route('/api/users', methods=['GET'])
def get_users():
    return jsonify([u.to_dict() for u in User.query.all()])

@user_bp.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = User(username=data['username'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201
