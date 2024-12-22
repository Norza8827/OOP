# LA 22
class Party:
    def __init__(self, theme, foods, special_dish):
        self.theme = theme
        self.foods = foods
        self.special_dish = special_dish
    def __specialDish(self):
        print(f"Special Dish: {self.special_dish}\n")
    def foodsList(self):
        print(f"{self.theme}")
        print(f"- {self.foods}")
        self.__specialDish()

Bday = Party("Birthday:", ["Cake, Lechon, Spaghetti"], "Lumpia")
Xmas = Party("Noche Buena:", ["Spaghetti, Carbonara, Lechon"], "Lumpia")
NewYear = Party("New Year:", ["Spaghetti, Menudo, Fruit Salad"], "Cordon Bleu")

Bday.foodsList()
Xmas.foodsList()
NewYear.foodsList()
