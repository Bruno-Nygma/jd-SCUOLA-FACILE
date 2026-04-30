from flask import jsonify, request, Blueprint
from service import student_service

student_bp = Blueprint("student", __name__)

# GET ALL STUDENTS
@student_bp.route("/api/students")
def get_students():

    students = student_service.get_all()

    return jsonify([s.to_dict() for s in students])


# GET STUDENT BY ID
@student_bp.route("/api/student/<student_id>")
def get_student_by_id(student_id):

    student_by_id = student_service.get_by_id(student_id)

    return jsonify(student_by_id.to_dict())


# CREATE STUDENT
@student_bp.route("/api/student", methods=["POST"])
def create():

    data = request.get_json() #Dal Body della richiesta
    
    try: 
        new_student = student_service.create(data)

        # 201 --> HTTP status code per "create"
        return jsonify(new_student.to_dict()), 201
    
    # 400 -> Richiesta non valida
    except ValueError as e: 
        return jsonify(str(e)), 400


# UPDATE STUDENT
@student_bp.route("/api/student/<student_id>", methods=["PATCH"])
def update(student_id):
    
    data = request.get_json() #Dal Body della richiesta
    updated = student_service.update(student_id, data)

    return jsonify(updated.to_dict())


# DELETE STUDENT BY ID
@student_bp.route("/api/student/<student_id>", methods=["DELETE"])
def delete_student_by_id(student_id):

    student_service.delete_by_id(student_id)

    return jsonify({"message":"student Eliminato"})