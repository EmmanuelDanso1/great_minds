from flask import Blueprint, request, jsonify
from models.courses import Course
from db import db

course_bp = Blueprint('course', __name__)

@course_bp.route('/api/courses', methods=['GET'])
def get_courses():
    return jsonify([c.to_dict() for c in Course.query.all()])

@course_bp.route('/api/courses', methods=['POST'])
def create_course():
    data = request.json
    new_course = Course(title=data['title'], description=data.get('description'))
    db.session.add(new_course)
    db.session.commit()
    return jsonify(new_course.to_dict()), 201
