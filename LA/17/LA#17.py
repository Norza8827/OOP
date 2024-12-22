# LA 17
class Player:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, target):
        if self.health <= 0:
            print(f"{self.name} cannot attack as they are defeated!")
            return
        if target.health <= 0:
            print(f"{target.name} is already defeated!")
            return
        
        target.health -= self.attack_power
        target.health = max(target.health, 0)
        print(f"{self.name} attacked {target.name} for {self.attack_power} damage!")
        print(f"{target.name}'s remaining health: {target.health}")
        if target.health == 0:
            print(f"{target.name} has been defeated!")

player1 = Player("Yasuo", 100, 15)
player2 = Player("Zed", 80, 20)

print("Battle Start!")
while player1.health > 0 and player2.health > 0:
    player1.attack(player2)
    if player2.health == 0:
        print(f"{player1.name} wins!")
        break

    player2.attack(player1)
    if player1.health == 0:
        print(f'''=================
{player2.name} wins!
=================''')
        break
