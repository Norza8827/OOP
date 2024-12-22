class hero():
    def __init__(self, name, role, dmg_type, health, auto_atk_dmg):
        self.name = name
        self.role = role
        self.dmg_type = dmg_type
        self.health = health
        self.auto_atk_dmg = auto_atk_dmg
        
    def describe(self):
        return f"{self.name} is a {self.role} with a {self.dmg_type} power"
    
    def __str__(self):
        return (f"{self.name} ({self.role})\n"
                f"Health: {self.health} HP\n"
                f"Basic Attack Damage: {self.auto_atk_dmg}\n"
                f"Damage Type: {self.dmg_type}\n"
                f"{self.describe()}")
        
hero_mm1 = hero("Moskov", "Marksman", "Physical Damage", 2255, 125)
hero_fighter1 = hero("Alpha", "Fighter", "Physical Damage", 2646, 121) 
hero_tank1 = hero("Jhonson", "Tank/Support", "Magic Damage", 2809, 120)
hero_assassin1 = hero("Ling", "Assassin", "Physical Damage", 2528, 125)
hero_mage1 = hero("Odette", "Mage", "Magic Damage", 2491, 105)

print(f'''
{hero_mm1}

{hero_fighter1}

{hero_tank1}

{hero_assassin1}

{hero_mage1}
''')