from flask import jsonify, request, Blueprint
from service import student_service
from exception.app_exception import AppException

student_bp = Blueprint("student", __name__, url_prefix="/api")

# GET ALL STUDENTS (con filtro opzionale per query params)
# ES: GET /api/students?corso=Informatica
@student_bp.route("/students")
def get_students():

    # Prendo il primo query param disponibile per filtrare
    course = request.args.get("course")

    if course:
        students = student_service.search_by_field("course", course)
    else:
        students = student_service.get_all()

    return jsonify([s.to_dict() for s in students])


# GET STUDENT BY ID
@student_bp.route("/student/<student_id>")
def get_student_by_id(student_id):

    try:
        student_by_id = student_service.get_by_id(student_id)

        return jsonify(student_by_id.to_dict())

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# CREATE STUDENT
@student_bp.route("/student", methods=["POST"])
def create():

    data = request.get_json() #Dal Body della richiesta

    try:
        new_student = student_service.create(data)

        # 201 --> HTTP status code per "create"
        return jsonify(new_student.to_dict()), 201

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# UPDATE STUDENT
@student_bp.route("/student/<student_id>", methods=["PATCH"])
def update(student_id):

    data = request.get_json() #Dal Body della richiesta

    try:
        updated = student_service.update(student_id, data)

        return jsonify(updated.to_dict())

    except AppException as e:
        return jsonify(e.to_dict()), e.status_code


# DELETE STUDENT BY ID
@student_bp.route("/student/<student_id>", methods=["DELETE"])
def delete_student_by_id(student_id):

    student_service.delete_by_id(student_id)

    return jsonify({"message": "Studente Eliminato"})