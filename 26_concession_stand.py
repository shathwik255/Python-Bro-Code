# Python Concession stand program

menu = {
    "pizza": 3.00,
    "nachos": 4.50,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}

cart = []
total = 0

print("---------- MENU ----------")
for item, price in menu.items():
    print(f"{item:10}: {price:.2f}")
print("--------------------------")

while True:
    food = input("Enter the food item(q or quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart += [food]

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total is: ${total:.2f}")
