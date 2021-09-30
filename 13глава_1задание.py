class Rectangle():
    def __init__(self, w, l):
        self.width=w
        self.len=l
    def calculate_perimeter(self):
        return self.width*2+self.len*2
    
class Square():
    def __init__(self, w):
        self.width=w
    def calculate_perimeter(self):
        return self.width*4
    
rectangle=Rectangle(10, 20)
print(rectangle.calculate_perimeter())
square=Square(10)
print(square.calculate_perimeter())
