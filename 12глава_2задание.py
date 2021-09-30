import math

class Circle():
    def __init__(self, r):
        self.radius = r**2

    def area(self):
        return self.radius * math.pi

circle = Circle(4)
print(circle.area())
