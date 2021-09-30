class Hexagon():
    def __init__(self, a, b, c, d, f, j):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.f = f
        self.j = j

    def calculate_perimeter(self):
        return self.a+self.b+self.c+self.d+self.f+self.j

hexadon = Hexagon(4, 4, 4, 4, 4, 4)
print(hexadon.calculate_perimeter())
