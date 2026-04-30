class Student(): 

    def __init__(self, id, name, surname, course, absence_percentage, email, password, img ):
        self.id = id
        self.name = name
        self.surname = surname 
        self.course = course 
        self.absence_percentage = absence_percentage
        self.email = email
        self.password = password
        self.img = img

    # TODO: Migliorare la stampa?
    def __str__(self): 
        return f"STUDENT: {self.id} {self.surname} {self.name} {self.email}"

    def __eq__(self, other):
        if not isinstance(other, Student): 
            return False
        
        # PK
        return self.id == other.id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "course": self.course,
            "absence_percentage": self.absence_percentage,
            "email": self.email,
            "password": self.password,
            "img": self.img
        }