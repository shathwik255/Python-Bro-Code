import random

options = ("rock", "paper", "scissors")
while True:
    comp = random.choice(options)
    usr = None
    while usr not in options:
        usr = input("Enter a choice (rock, paper, scissors): ").lower()

    if usr == comp:
        print("It's a tie!")
    elif (usr == "rock" and comp == "scissors") or (usr == "paper" and comp == "rock") or (usr == "scissors" and comp == "paper"):
        print("You win!")
    else:
        print("You lose!")
    play_again = input("Play again? (y/n): ").lower()
    if not play_again == "y":
        break

print("Thanks for playing!")
