# LA 26 (file 1)
from abc import ABC, abstractmethod

class NinjaTurtles(ABC):
    @abstractmethod
    def etc(self):
        pass

class Leonardo(NinjaTurtles):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias    
    def etc(self):
        return f"{self.__alias}" 
    
class Michaelangelo(NinjaTurtles):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias    
    def etc(self):
        return f"{self.__alias}" 
    
class Donatello(NinjaTurtles):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias    
    def etc(self):
        return f"{self.__alias}" 
    
class Raphael(NinjaTurtles):
    def __init__(self, real_name, alias):
        self.real_name = real_name
        self.__alias = alias    
    def etc(self):
        return f"{self.__alias}" 