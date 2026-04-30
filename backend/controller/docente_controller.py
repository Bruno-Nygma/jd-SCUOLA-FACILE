from flask import jsonify,request,Blueprint
from service import docente_service

docente_bp = Blueprint("docenti", __name__)

@docente_bp.route("/docenti")
def get_docenti():
    return docente_service.get_all_docenti()

@docente_bp.route("/docenti", methods = ["POST"])
def create_docente():

    docente = request.get_json()
    return jsonify(docente_service.create_docente(docente)), 201

@docente_bp.route("/docenti/<int:docente_id>")
def get_docente_by_id(docente_id):
    return docente_service.get_docente_by_id(docente_id), 201

@docente_bp.route("/docenti/<int:student_id>", methods = ["DELETE"])
def delete_docente(docente_id):
    return docente_service.get_docente_by_id(docente_id)

@docente_bp.route("/studenti/<int:student_id>", methods = ["PATCH"])
def update_docente(docente_id):

    docente_data = request.get_json()
    return docente_service.update_docente(docente_id, docente_data)