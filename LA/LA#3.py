# OOP LA 3

class hero:
   def __init__(self, name):
      self.name = name
      
   def describe(self, role):
      print(f"{self.name} is a {role} hero.")
      
hero_name = hero("Alpha")
hero_name.describe("Fighter")