from model.person import Person


# Docente
class Teacher(Person):

    def __init__(self, id, name, surname, course, email, password, img):
        super().__init__(id, name, surname, email, password)
        self.course = course
        self.img = img

    # base perchè è classe che eredita da Persona e quindi parte già da una base
    def to_dict(self):
        base = super().to_dict()
        base["course"] = self.course
        base["img"] = self.img

        return base