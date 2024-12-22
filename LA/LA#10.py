# LA 10
class Vehicle():
    def __init__(self, brand, model, fuel_type):
        self.brand = brand
        self.model = model
        self.fuel_type = fuel_type
    def describeVehicle(self):
        print(f'''Brand: {self.brand}
Model: {self.model}
Fuel type: {self.fuel_type}
''')
        
class Car(Vehicle):
    pass

mclaren = Car("McLaren", "P1", "Petrol/Hybrid")
mclaren.describeVehicle()

class Motorcycle(Vehicle):
    pass

honda = Car("Honda", "Click", "Gasoline")
honda.describeVehicle()
