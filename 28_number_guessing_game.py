# Python Number Guessing Game

import random

min_num = 1
max_num = 100
answer = random.randint(min_num, max_num)
guesses = 0

print("Python Number Guessing Game")
print(f"Select a number between {min_num} and {max_num}")

while True:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < min_num or guess > max_num:
            print(f"{guess} is out of range")
            print(f"Please select a number between {min_num} and {max_num}")
        elif guess < answer:
            print("Too low! Try again!")
        elif guess > answer:
            print("Too High! Try again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"You have guessed the number in {guesses} guesses")
            break
    else:
        print("Invalid guess")
        print(f"Please select a number between {min_num} and {max_num}")
