import random

HIGHEST_NUMBER = 100
LOWEST_NUMBER = 1

VERSION = "v2.0.0"
AUTHOR = "meteor"

CHEAT = False

randomnum = random.randint(LOWEST_NUMBER, HIGHEST_NUMBER)
attempts = 0

print(f"Number Guessing Game | {VERSION}")
print(f"Author: {AUTHOR}")
print("Status: ✅")
if CHEAT == True:
    print(f"Number: {randomnum}")
print("")
def victory():
    if guess == randomnum and attempts == 1:
        print(f"You have guessed the correct number in one attempt, wow!")
        exit()
    elif guess == randomnum:
        print(f"You have guessed the correct number in {attempts} attempts.")
        exit()
def checks():
    if guess < randomnum:
        print("Try higher")
    elif guess > randomnum:
        print("Try lower")

while True:
    HIGHEST_NUMBER = str(HIGHEST_NUMBER)
    LOWEST_NUMBER = str(LOWEST_NUMBER)
    guess = input("I am thinking of a number between " + LOWEST_NUMBER + "-" + HIGHEST_NUMBER + ", can you try and guess it? ")
    if guess.isdigit():
        attempts += 1
        guess = int(guess)
        checks()
        victory()
    else:
        print("That is an invalid number!")
