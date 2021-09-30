import math

class Triangle():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return math.sqrt((self.a+self.b+self.c)/2*(((self.a+self.b+self.c)/2)-self.a)*(((self.a+self.b+self.c)/2)-self.b)*(((self.a+self.b+self.c)/2)-self.c))

triangle = Triangle(4, 4, 6)
print(triangle.area())
