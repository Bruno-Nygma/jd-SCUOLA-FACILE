from model.student import Student

# Classe temporanea che simula un datrabase - Operazioni CRUD 
# DummyDB è il mio "template" di database
class DummyDB: 

    def __init__(self): 
        # Attributo privato perchè non dovrei accederci da fuori
        # self._next_id = 1 tolto perchè dal FE id è alfanumerico (stringa )
        self._data = {}

    # Il return di s è superlfuo in questo caso in quanto l'id non è auto calcolato dal database
    def create(self, s): 
        self._data[s.id] = s
        
        return s
    
    def get_all(self): 
        return list(self._data.values())
    
    def get_by_id(self, id): 
        return self._data.get(id) # Il mio DB è un dizionario che ha come chiave proprio entità_id

    # Aggiorno solo i campi che mi arrivano. 
    # ES: Se non passo il nome, non viene aggiornato
    def update(self, id, updates): 
        record_2_update = self._data.get(id)

        for k, v in updates.items(): 
            setattr(record_2_update, k, v)
        
        return record_2_update
    
    # DELETE FROM student WHERE student_id = $student_id
    def delete_by_id(self, id): 
        return self._data.pop(id, None)

    
studenti_db = DummyDB()
docenti_db = DummyDB()

dataset_test_students = [
    Student("STU-017", "Lorenzo", "Giordano", "Informatica", 16, "lorenzo.giordano@example.com", "password123!", "https://api.dicebear.com/9.x/initials/svg?seed=Lorenzo-Giordano" ), 
    Student("STU-018", "Silvia", "Rizzo", "Economia", 25, "silvia.rizzo@example.com", "password123!", "https://api.dicebear.com/9.x/initials/svg?seed=Silvia-Rizzo" )
]

for s in dataset_test_students: 
    studenti_db.create(s)