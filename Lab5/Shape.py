from math import sqrt
from math import pi


class Shape:

    def __init__(self, color):
        self.color = color


class Circle(Shape):

    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):

    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        return area

    def calculate_perimeter(self):
        perimeter = 2 * self.length + 2 * self.width
        return perimeter


class Triangle(Shape):

    def __init__(self, color, a, b, c):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def calculate_area(self):
        demi_perimeter = self.calculate_perimeter() / 2
        area = sqrt(
            demi_perimeter * (demi_perimeter - self.a) * (demi_perimeter - self.b) * (demi_perimeter - self.c))
        return area

    def calculate_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter
