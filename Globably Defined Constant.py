class Person:

    number_of_persons_ = 0    # Globally defined constants
    gravity = -9.8

    def __init__(self, name):
        self.name = name
        Person.Add_person()

    @classmethod
    def number_of_persons(cls):
        return cls.number_of_persons_()

    @classmethod
    def Add_person(cls):
        cls.number_of_persons_ += 1
    

print(Person.number_of_persons_)
print(Person.gravity)
p1 = Person("Jimme")
print(Person.number_of_persons_)
print(Person.gravity)
p2 = Person("John")
print(Person.number_of_persons_)
print(Person.gravity)
Person.Add_person()
Person.Add_person()
print(Person.number_of_persons_)
