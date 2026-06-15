import random

print("Higher Lower Game Starts...")

random_number = random.randint(1, 100)

guess_number = int(input("Guess a number between 1 and 100: "))
number_of_guesses = 0

while guess_number != random_number:

    if guess_number < random_number:
        print("Higher")
    else:
        print("Lower")

    number_of_guesses += 1
    guess_number = int(input("Guess a number between 1 and 100: "))

print("Congratulations! You guessed the number correctly.")
print("The random number was:", random_number)
print("Number of guesses:", number_of_guesses)