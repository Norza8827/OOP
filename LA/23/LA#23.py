# LA 23
class AnimeCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def introduce(self, func):
        def char_name(*args, **kwargs):
            print(f"Introducing...")
            func(*args, **kwargs)
            print(f"This character is suffering! ToT")
        return char_name
       
character1 = AnimeCharacter("Natsuki Subaru", "Return by Death")
@character1.introduce
def intro(name, ability):
    print(f"My name is {name}! I can use {ability}!")
intro("Natsuki Subaru", "Return by Death")