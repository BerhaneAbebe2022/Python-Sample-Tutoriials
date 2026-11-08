from abc import ABC, abstractmethod


class shape:

    @abstractmethod
    def area(self):
        pass
        
class Circle(shape):

    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius * self.radius

class Square(shape):

    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side**2

class Triangle(shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height * 0.5
class Pizza(Circle):

    def __init__(self, topping, radius):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(5), Square(4), Triangle(4, 6), Pizza("Pepporeni", 10)]

for shape in shapes:
    print(shape.area())
