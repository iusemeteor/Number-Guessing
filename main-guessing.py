import random

randomnum = random.randint(1, 10)
attempts = 0
print(randomnum)

while True:
    guess = input("Give me a number between 1-10: ")
    if guess.isdigit():
        attempts += 1
        guess = int(guess)
        if guess < randomnum:
            print("Try higher")
        elif guess > randomnum:
            print("Try lower")
        if guess == randomnum and attempts == 1:
            print(f"You have guessed the correct number in one attempt, ggs.")
            break
        elif guess == randomnum:
            print(f"You have gussed the correct number in {attempts} attempts.")
            break
    else:
        print("That's not a number")
