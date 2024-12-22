# LA 16
class Appliance:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def operate(self):
        print("Operating!")
    
    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

class WashingMachine(Appliance):
    def operate(self):
        print("Washing Machine: Washing clothes!")

class Refrigerator(Appliance):
    def operate(self):
        print("Refrigator: Keeping food cold!")

class Microwave(Appliance):
    def operate(self):
        print("Microwave: Heating food!")

washing_machine = WashingMachine("LG", "TwinWash")
refrigerator = Refrigerator("Samsung", "Family Hub")
microwave = Microwave("Panasonic", "Inverter")

appliances = [washing_machine, refrigerator, microwave]

for appliance in appliances:
    appliance.operate()

print("\nAppliances Info:")
for appliance in appliances:
    appliance.info()
