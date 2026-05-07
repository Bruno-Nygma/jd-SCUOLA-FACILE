from repository import teacher_repository
from model.teacher import Teacher
from exception.app_exception import AppException


def create(data):
    _validate_teacher(data)

    # Controllo duplicati per id
    if teacher_repository.get_by_id(data["id"]) is not None:
        raise AppException("Docente con questo id esiste già!", 409)

    teacher_2_create = Teacher(data["id"],
                               data["name"],
                               data["surname"],
                               data["course"],
                               data["email"],
                               data["password"],
                               data["img"])

    return teacher_repository.create(teacher_2_create)

def get_all():
    return teacher_repository.get_all()

def get_by_id(teacher_id):
    teacher = teacher_repository.get_by_id(teacher_id)

    if teacher is None:
        raise AppException("Docente non trovato!", 404)

    return teacher

def update(teacher_id, data):
    if "password" in data:
        _validate_teacher(data)

    updated = teacher_repository.update_teacher(teacher_id, data)

    if updated is None:
        raise AppException("Docente non trovato!", 404)

    return updated

def delete_by_id(teacher_id):
    teacher_repository.delete_by_id(teacher_id)

def _validate_teacher(data_teacher):

    #img default
    if "img" not in data_teacher:
        data_teacher["img"] = f"https://api.dicebear.com/9.x/initials/svg?seed={data_teacher["name"].replace(" ", "")}-{data_teacher["surname"]}"

    # Campi obbligatori
    for field in ["name", "surname", "email"]:
        if field not in data_teacher or len(data_teacher[field].strip()) == 0:
            raise AppException(f"Campo '{field}' obbligatorio!", 400)

    # Formato email
    if "@" not in data_teacher["email"] or "." not in data_teacher["email"]:
        raise AppException("Formato email non valido!", 400)

    # Password
    if "password" not in data_teacher:
        raise AppException("Password mancante!", 400)

    if len(data_teacher["password"]) < 4:
        raise AppException("Password troppo corta!", 400)