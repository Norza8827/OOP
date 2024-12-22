# LA 13
class Animal():
    def __init__(self, name, type, can_swim):  
        self.name = name
        self.type = type

    def describeAnimal(self):
        print(f'''Name: {self.name} 
Type: {self.type}
Can swim: {self.can_swim}
''')

class Fish(Animal):
    def __init__(self, name, type, can_swim): 
        self.can_swim = True
        super().__init__(name, type, can_swim)

bangus = Fish("Bangus", "Fish", True)
bangus.describeAnimal()
