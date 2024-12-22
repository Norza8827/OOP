#  LA 24
from abc import ABC, abstractmethod
class GameCharacter(ABC):
    def __init__(self, name, move):
        super().__init__()
        self.name = name
        self.move = move
    @abstractmethod
    def attack(self):
        pass

class Warrior(GameCharacter):
    def attack(self):
        print(f"{self.name}: {self.move}")

class Mage(GameCharacter):
    def attack(self):
        print(f"{self.name}: Casts a {self.move}")

class Archer(GameCharacter):
    def attack(self):
        print(f"{self.name}: Shoots an {self.move}")

warrior_attack = Warrior("Warrior", "Swing Sword!")
mage_attack = Mage("Mage", "Fireball!")
archer_attack = Archer("Archer", "Shoot an Arrow!")
warrior_attack.attack()
mage_attack.attack()
archer_attack.attack()
