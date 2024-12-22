# LA 15
class Dog:
  def __init__(self, name):
      self.name = name
  def speak(self):
      print(f'''{self.name}: Bark!''')

class Cat:
  def __init__(self, name):
      self.name = name
  def speak(self):
      print(f'''{self.name}: Meow!''')

class Bird:
  def __init__(self, name):
      self.name = name
  def speak(self):
      print(f'''{self.name}: Chirp!''')

class Fish:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(f'''{self.name}: ...''')

def animal_sounds(Dog, Cat, Bird):
    Dog.speak()
    Cat.speak()
    Bird.speak()
    Fish.speak()
    pass

dog = Dog("Dog")
cat = Cat("Cat")
bird = Bird("Bird")
fish = Fish("Fish")

for x in [dog, cat, bird, fish]:
  x.speak()
