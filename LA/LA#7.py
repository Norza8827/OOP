# LA 7
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

car1 = Car("Toyota", "Black")
car2 = Car("McLaren", "White")

print(f"Original value: {car1.brand} {car1.color}")
# print(f"Original value: {car2.brand} {car2.color}")
print("--------------------------------------")

car1.color = "Blue"

print(f"Updated value: {car1.brand} {car1.color}")
print(f"Updated value: {car2.brand} {car2.color}")