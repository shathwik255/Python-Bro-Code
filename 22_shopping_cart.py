foods = []
prices = []

while True:
    food = input("Enter the food (q to quit): ")
    if food == "q":
        break
    price = float(input(f"Enter the price of {food}: $"))
    foods.append(food)
    prices.append(price)

print("----- YOUR CART -----")
for food in foods:
    print(food, end=" ")
print()
total = 0
for price in prices:
    total += price
print(f"Your total is: {round(total, 2)}")
