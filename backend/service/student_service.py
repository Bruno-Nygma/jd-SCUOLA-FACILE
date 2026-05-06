from repository import student_repository
from model.student import Student
from exception.app_exception import AppException


# data viene dalla request HTTP, non è ancora un reale oggetto Python di tipo Student
def create(data):
    _validate_student(data)

    # Controllo duplicati per id
    if student_repository.get_by_id(data["id"]) is not None:
        raise AppException("Studente con questo id esiste già!", 409)

    # Controllo duplicati per email
    existing = student_repository.get_by_field("email", data["email"])
    if len(existing) > 0:
        raise AppException("Email già registrata!", 409)

    # "converto" oggetto dalla richiesta HTTP ad un oggetto di tipo Studente perché il repo si aspetta già uno studente
    student_2_create = Student(data["id"],
                               data["name"],
                               data["surname"],
                               data["course"],
                               data["absence_percentage"],
                               data["email"],
                               data["password"],
                               f"https://api.dicebear.com/9.x/initials/svg?seed={data["name"]}-{data["surname"]}")

    return student_repository.create(student_2_create)

def get_all():
    return student_repository.get_all()

def get_by_id(student_id):
    student = student_repository.get_by_id(student_id)

    if student is None:
        raise AppException("Studente non trovato!", 404)

    return student

# Ricerca studenti per campo (es: corso=Informatica)
def search_by_field(field, value):
    return student_repository.get_by_field(field, value)

def update(student_id, data):
    if "password" in data:
        _validate_student(data)

    updated = student_repository.update_student(student_id, data)

    if updated is None:
        raise AppException("Studente non trovato!", 404)

    return updated

def delete_by_id(student_id):
    student_repository.delete_by_id(student_id)

# Qui metto tutti i vincoli che mi potrei anche sul DB (chiavi not null, vincoli numerici ect ect )
# data_student perchè non ho uno studente, ho "data" che mi arriva dal FE
def _validate_student(data_student):

    # Campi obbligatori
    for campo in ["name", "surname", "email"]:
        if campo not in data_student or len(data_student[campo].strip()) == 0:
            raise AppException(f"Campo '{campo}' obbligatorio!", 400)

    # Formato email
    if "@" not in data_student["email"] or "." not in data_student["email"]:
        raise AppException("Formato email non valido!", 400)

    # Vincolo: pwd > 4 caratteri
    if "password" not in data_student:
        raise AppException("Password mancante!", 400)

    if len(data_student["password"]) < 4:
        raise AppException("Password troppo corta!", 400)