# OOP LA 2

class hero:
   def __init__(self, name, role):
      self.name = name
      self.role = role
      
hero_info = hero("Alpha", "Fighter")
print(hero_info.name, hero_info.role)
