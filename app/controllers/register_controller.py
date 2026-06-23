#
from flask import jsonify, request
from app.extensions import db
from app.models.register_model import Student


from werkzeug.security import generate_password_hash


def set_password(pwd):
        password = generate_password_hash(pwd)
        return password


def _validate_student_payload(data, student_id=None):
    errors = []
    if not data:
        return ["Request body is required."]


    email = data.get("email")
    if email is None or str(email).strip() == "":
        errors.append("email is required.")
    elif str(email).strip():
        q = Student.query.filter(Student.email == str(email).strip())
        if student_id:
            q = q.filter(Student.id != student_id)
        if q.first():
            errors.append("Email address already exists.")
    return errors


def create_student():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Request body is required."}), 400

    errors = _validate_student_payload(data)
    if errors:
        return jsonify({"errors": errors}), 400

    try:
        student = Student(
            email=data.get("email").strip(),
            password=set_password(data.get("password")).strip()
            
        )
        db.session.add(student)
        db.session.commit()
        return jsonify({"message": "Student created successfully.", "student": student.to_dict()}), 201
    except Exception:
        db.session.rollback()
        return jsonify({"error": "An internal server error occurred."}), 500




