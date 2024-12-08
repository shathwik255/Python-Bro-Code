import random

# print(help(random))
# min = 1
# max = 100
# random_number = random.randint(min, max)
# random_number = random.random()
# print(random_number)

# options = ("rock", "paper", "scissors")
# option = random.choice(options)
# print(option)

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)
