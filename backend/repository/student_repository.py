from persistence.dummy_db import students_db

def create(student):
    return students_db.create(student)

def get_all():
    return students_db.get_all()

def get_by_id(student_id):
    return students_db.get_by_id(student_id)

# Cerca studenti per un campo specifico (es: "corso", "Informatica")
def get_by_field(field, value):
    return students_db.get_by_field(field, value)

def update_student(student_id, data):
    return students_db.update(student_id, data)

def delete_by_id(student_id):
    return students_db.delete_by_id(student_id)