import json
import os

from model.student import Student
# from model.teacher import Teacher
# from model.course import Course

# Classe temporanea che simula un datrabase - Operazioni CRUD
# DummyDB è il mio "template" di database
class DummyDB:

    def __init__(self):
        # Attributo privato perchè non dovrei accederci da fuori
        self._data = {}

    # Il return di s è superlfuo in questo caso in quanto l'id non è auto calcolato dal database
    def create(self, s):
        self._data[s.id] = s

        return s

    def get_all(self):
        return list(self._data.values())

    def get_by_id(self, id):
        return self._data.get(id) # Il mio DB è un dizionario che ha come chiave proprio entità_id

    # Cerca tutti i record che hanno un certo valore su un certo campo
    # ES: get_by_field("corso", "Informatica") -> tutti gli studenti del corso Informatica
    def get_by_field(self, field, value):
        results = []

        for record in self._data.values():
            if hasattr(record, field) and getattr(record, field) == value:
                results.append(record)

        return results

    # Aggiorno solo i campi che mi arrivano.
    # ES: Se non passo il nome, non viene aggiornato
    def update(self, id, updates):
        record_2_update = self._data.get(id)

        if record_2_update is None:
            return None

        for k, v in updates.items():
            setattr(record_2_update, k, v)

        return record_2_update

    # DELETE FROM student WHERE student_id = $student_id
    def delete_by_id(self, id):
        return self._data.pop(id, None)


students_db = DummyDB()
teachers_db = DummyDB()
courses_db = DummyDB()

# ---- Caricamento dati di test da file JSON ----

# os.path.dirname(__file__) restituisce la cartella dove si trova dummy_db.py
_dataset_dir = os.path.join(os.path.dirname(__file__), "dataset")

with open(os.path.join(_dataset_dir, "students.json")) as f:
    for s in json.load(f):
        students_db.create(Student(s["id"], s["name"], s["surname"], s["course"],
                                   s["absence_percentage"], s["email"], s["password"], s["img"]))

# with open(os.path.join(_dataset_dir, "teachers.json")) as f:
#     for t in json.load(f):
#         teachers_db.create(Teacher(t["id"], t["nome"], t["cognome"], t["materia"],
#                                    t["email"], t["password"]))

# with open(os.path.join(_dataset_dir, "courses.json")) as f:
#     for c in json.load(f):
#         courses_db.create(Course(c["id"], c["nome"], c["descrizione"],
#                                  c["docente_id"], c["studenti_ids"]))