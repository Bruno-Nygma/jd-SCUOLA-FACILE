from repository import student_repository
from model.student import Student


# data viene dalla request HTTP, non è ancora un reale oggetto Python di tipo Student
def create(data): 
    _validate_student(data)

    # "converto" oggetto dalla richiesta HTTP ad un oggetto di tipo student perché il repo si aspetta già uno student
    student_2_create =  Student(
        data["id"], 
        data["name"],
        data["surname"],
        data["course"], 
        data["absence_rate"], 
        data["email"], 
        data["password"], 
        None
    )
    
    return student_repository.create(student_2_create)

def get_all(): 
    return student_repository.get_all()

def get_by_id(student_id): 
    return student_repository.get_by_id(student_id)

def update(student_id, data): 
    _validate_student(data)
    
    return student_repository.update_student(student_id, data)

def delete_by_id(student_id): 
    return student_repository.delete_by_id(student_id)

# Qui metto tutti i vincoli che mi potrei anche sul DB (chiavi not null, vincoli numerici ect ect )
# data_student perchè non ho uno student, ho "data" che mi arriva dal FE
def _validate_student(data_student): 

    # Vincolo 1: pwd > 4 caratteri
    if "password" not in data_student: 

        raise ValueError("Password mancante!") #TODO: Mettere Error custom
    
    if len(data_student["password"]) < 4:
        
        raise ValueError("Password troppo corta!") #TODO: Mettere Error custom