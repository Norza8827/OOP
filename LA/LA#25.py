from abc import ABC, abstractmethod

class Character(ABC):   
    @abstractmethod
    def etc(self):
        pass

class Batman(Character):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias    
    def etc(self):
        return f"{self.__alias}" 
    
bats = Batman("Bruce Wayne", "Batman")
print(bats.etc())