from persistence.dummy_db import teachers_db

def create(teacher):
    return teachers_db.create(teacher)

def get_all():
    return teachers_db.get_all()

def get_by_id(teacher_id):
    return teachers_db.get_by_id(teacher_id)

def update_teacher(teacher_id, data):
    return teachers_db.update(teacher_id, data)

def delete_by_id(teacher_id):
    return teachers_db.delete_by_id(teacher_id)