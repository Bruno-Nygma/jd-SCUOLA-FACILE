from dummy_db import studenti_db

def create(student): 
    return studenti_db.create(student)

def get_all(): 
    return studenti_db.get_all()

def get_by_id(student_id): 
    return studenti_db.get_by_id(student_id)

def update_student(student_id, data): 
    return studenti_db.update(student_id, data)

def delete_by_id(student_id): 
    studenti_db.delete_by_id(student_id)