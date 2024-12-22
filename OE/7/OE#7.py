class TekkenCharacter:
    def __init__(self, name, ability):
        self.name = name
        self.ability = ability
    def introduce(self, func_name):
        def payt(*args, **kwargs):
            print("Introducing...")
            func_name(*args, **kwargs)
            print("This character is amazing!")
        return payt
    
nina = TekkenCharacter("Nina", "Fatal Judgement")

@nina.introduce
def character_intro():
    print(f"I am {nina.name} and I can use {nina.ability}.")

character_intro()
