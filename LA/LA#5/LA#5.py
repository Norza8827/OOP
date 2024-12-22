class Hero:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    
    def __str__(self):
        return f"This is character objetct."
    
    def describe(self):
        return f"{self.name} is a {self.role} hero."

hero_name = Hero("Alpha", "Fighter")
print(hero_name.describe())
