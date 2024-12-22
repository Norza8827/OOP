# OE 2
class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f"{self.brand} {self.model} {self.price}"

phones = []

while True:
    print("\n===============")
    print("  Main Menu:")
    print("===============")
    print("1. Add Phone")
    print("2. Modify Phone")
    print("3. Delete Phone")
    print("4. View Phones")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == '1':
        brand = input("Enter the Brand: ")
        model = input("Enter the Model: ")
        price = (input("Enter the Price: "))
        phones.append(Phone(brand, model, price))
    elif choice == '2':
        if not phones:
            print("There are no phones to modify.")
            continue
        for selpon, phone in enumerate(phones):
            print(f"{selpon+1}. {phone}")
        index = int(input("Enter the phone number to modify: ")) - 1
        if 0 <= index < len(phones):
            phones[index].brand = input("Enter the new brand (leave a blank to cancel): ") or phones[index].brand
            phones[index].model = input("Enter the new model (leave a blank to cancel): ") or phones[index].model
            new_price = input("Enter the new price (leave a blank to cancel): ")
            phones[index].price = (new_price) if new_price else phones[index].price

        else:
            print("Invalid phone number!.")

    elif choice == '3':
        if not phones:
            print("There are no phones to delete.")
            continue
        for selpon, phone in enumerate(phones):
            print(f"{selpon+1}. {phone}")
        index = int(input("Enter the phone number to delete: ")) - 1
        if 0 <= index < len(phones):
            del phones[index]
        else:
            print("Invalid phone number!")
    elif choice == '4':
        if not phones:
            print("There are currently no Phones in this list.")
        else:
            for phone in phones:
                print(phone)
    elif choice == '5':
        break
    else:
        print("\nInvalid choice! Please enter a valid option.")
