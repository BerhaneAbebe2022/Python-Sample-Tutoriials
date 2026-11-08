class shape:

    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is a {self.color} and It is {'filled' if self.is_filled else 'not filled'}")
        
class Circle(shape):

    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
    def describe(self):
        super().describe()
        print(f"The area of the circle is {3.14 * self.radius**2} cm^2")

class Square(shape):

    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
    def describe(self):
        super().describe()
        print(f"The area of the Square is {self.width**2} cm^2")

class Triangle(shape):

    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
    def describe(self):
        super().describe()
        print(f"The area of the Triangle is {3.14 * self.width * self.height / 2} cm^2")

circle = Circle("red", True, 5)
square = Square("blue", False, 6)
triangle = Triangle("green", True, 4, 5)
