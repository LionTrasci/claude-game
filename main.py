### Base game based on what claude told us to make

### if we want to pipinstall any additional libraries we need to declare them in the requirements.txt file
import random

def play():
    secret = random.randint(1, 100)
    guesses = 0
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Your guess: "))
        guesses += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"You got it in {guesses} guesses!")
            break

if __name__ == "__main__":
    play()