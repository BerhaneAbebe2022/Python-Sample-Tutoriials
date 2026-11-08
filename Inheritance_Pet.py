class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} Years old")

    def speak(self):
        print("I do not know what to say")

class Cat(Pet):        # inherit the properties of a class pet
    
    def __init__(self, name, age, color):
        super().__init__(name, age)    # inherit already defined in the parent class
        self.color = color
        
    def speak(self):   # If a method is defined in both the parent and child class,
        print("Meow")  # the child overridees the parent class

    def show(self):
        print(f"I am {self.name} and I am {self.age} Years old, and my color is {self.color}.")
        
class Dog(Pet):        # inherit the properties of a class pet

    def speak(self):
        print("Bark")

p = Pet("Bill", 10)
d = Dog("Tim", 6)
c = Cat("Rocky", 8, "Brown")
p.show()
c.show()
d.show()
p.speak()
c.speak()
d.speak()

