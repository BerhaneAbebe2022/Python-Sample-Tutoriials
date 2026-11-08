class Animal:

    alive = True

class Dog(Animal):

    def speak(self):
        print("Woof")

class Cat(Animal):

    def speak(self):
        print("Moew")

class Car:
    
    alive = False
    
    def speak(self):
        print("hunt")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
