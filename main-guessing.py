import random

def main():
    print("Welcome to the meteor guessing game")
    print("I'm thinking if a number between 1 and 10.")

    random_number = random.randint(1, 10)
    guess = None
    attempts = 0

    while guess != random_number:
        try:
            guess = int(input("Guess the number: "))
            attempts += 1
            if guess > random_number:
                print("That is too high!")
            elif guess < random_number:
                print("That is too low!")
            else:
                print(f"You have guessed the number in {attempts} attempts.")
        except ValueError:
            print("That is an invalid number!")

if __name__ == '__main__':
    main()