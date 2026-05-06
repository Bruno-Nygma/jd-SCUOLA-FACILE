from model.person import Person


# Campi in italiano per via del FE, andrebbero rimappati in inglese
class Student(Person):

    def __init__(
        self, id, name, surname, course, absence_percentage, email, password, img
    ):
        super().__init__(id, name, surname, email, password)
        self.course = course
        self.absence_percentage = absence_percentage
        self.img = img

    # to_dict per la conversione che serve al metodo jsonify
    def to_dict(self):

        # base perchè è classe che eredita da Persona e quindi parte già da una base
        base = super().to_dict()
        base["course"] = self.course
        base["absence_percentage"] = self.absence_percentage
        base["img"] = self.img

        return base