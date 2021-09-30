class Square():
    def __init__(self, w):
        self.width=w*4
        
    def change_size(self):
        if self.width <0:
            return self.width*(-1)
        else:
            return self.width

square=Square(-10)
print(square.change_size())

