class Horse():
    def __init__(self, name,breed, owner):
       self.name=name
       self.breed=breed
       self.owner=owner

class Rider():
    def __init__(self, name):
        self.name=name

nick=Rider("Nick McConnell")
milo=Horse("Milo", "English horse", nick)

print(milo.owner.name)
