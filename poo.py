class Person():
    name = ""
    age = 0
    color_pelo = ""
    __numero_telefono = ""
    def __init__(self, color, name=None, age=None):
        self.name = name
        self.age = age
        self.color_pelo = color
personal = Person("negro", "Miguel", "53")
personal.__numero_telefono = 6753345

print(personal.color_pelo, personal.name, personal.__numero_telefono)

class User(Person):

    def __init__(self, color, name=None, age=None):
        super(User, self).__init__(color, name=name, age=age)

user1 = User("Rojo" , "Miguel")

print("Hijo ", user1.color_pelo, user1.name)


class Person():
    name = ""
    age = 10
    color_pelo = ""
    __numero_telefono = ""
    def __init__(self, color, name=None):
        self.name = name
        self.color_pelo = color
personal = Person("negro", "Miguel")
personal.__numero_telefono = 6753345

print(personal.color_pelo, personal.name, personal.__numero_telefono)
# Herencia

class User(Person):
    age = 20

    def __init__(self, color, name=None):
        super(User, self).__init__(color, name=name)

user1 = User("Rojo" , "Miguel")

print("Hijo ", user1.color_pelo, user1.name, user1.age)