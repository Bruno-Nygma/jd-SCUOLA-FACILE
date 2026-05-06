from persistence.dummy_db import docenti_db

def get_all_docenti():
    return docenti_db.get_all()

def create_docente(docente):
    return docenti_db.create(docente)

def get_docente_by_id(docente_id):
    return docenti_db.get_by_id(docente_id)

def delete_docente(docente_id):
    return docenti_db.delete(docente_id)

def update_docente(docente_id, docente_data):
    return docenti_db.alter(docente_id, docente_data)