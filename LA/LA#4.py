# OOP LA 4

class hero:
   def __init__(self, name):
      self.name = name     
  
    def __str__(self):
      return "This is character object."
      
   def describe(self, role):
      print(f"{self.name} is a {role} hero.")
      
hero_name = hero("Alpha")
print(hero_name())