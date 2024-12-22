# OE 4
class Character:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
        
    def attack(self, target):
        target.health -= self.power
        print(f"{self.name} attacks {target.name}! {target.name} has only {target.health} HP remaining.")
        
    def special_move(self, target):
        pass
        
    def defend(self, attacker):
        self.health -= attacker.power

class Warrior(Character):
    def special_move(self, target):
        print(f"{self.name} used Shield Bash! ATK power has been doubled.")
        self.power *= 2

class Mage(Character):
    def special_move(self, target):
        print(f"{self.name} casts Fireball! Monster's HP has been reduced by 100.")
        target.health -= 100

class Archer(Character):
    def special_move(self, target):
        print(f"{self.name} shoots a Piercing Arrow! Monster's defense has been ignored.")
        self.power *= 1.5

class Monster(Character):
    def special_move(self, target):
        print(f"{self.name} roars and regained 50 HP!")
        self.health += 50

warrior = Warrior("Warrior", 300, 40)
mage = Mage("Mage", 220, 30)
archer = Archer("Archer", 245, 35)
monster = Monster("Monster", 400, 50)
characters = [warrior, mage, archer]

while True:
    for attacker in characters:
        attacker.attack(monster)
        attacker.special_move(monster)
        monster.defend(attacker)
        if monster.health <= 0:
            print("Monster has been Defeated!")
            exit()
            
    for character in characters[:]:
        monster.attack(character)
        monster.special_move(character)
        character.defend(monster)
        if character.health <= 0:
            print(f"{character.name} has been Defeated!")
            characters.remove(character)
            
    if not characters:
        print("Monster Wins!")
        break
