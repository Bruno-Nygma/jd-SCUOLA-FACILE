# Classe base per Student e Teacher (che ereditano)
class Person:

    def __init__(self, id, name, surname, email, password):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def __str__(self):
        return f"{self.__class__.__name__}: {self.id} {self.surname} {self.name} {self.email}"

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.id == other.id

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "password": self.password,
        }