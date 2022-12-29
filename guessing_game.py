# QUESTION : Guessing game where the computer has a secret number .And we are trying to guess the secret number .                     .

# so the first step is actually having the Generate a secret number for us to guess.And in order
# to do that, we are going to import random.
# Whenever we call import random, it actually goes to this package that comes with python.And it says,
# Hey,all of these functions that are here

#  random.randint(a,b) it means, return a random number integer N such that a <= N <= b.

import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {x}: "))

        if guess < random_number:
            print("Sorry, Guess again.It's too low.")
        elif guess > random_number:
            print("Sorry, Guess again.It's too high.")
        else:
            print(f"Yay, Congrats. You have guessed the number {random_number} correctly!")


guess(10)

# QUESTION : Guessing game where I have a secret number .And the computer is trying to guess the secret number .


def computer_guesses_range(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':   # c for correct
        if low != high:
            comp_guess = random.randint(low,high)
        else:
            comp_guess = low  # could also be high bcz low = high
        feedback = input(f"Is {comp_guess} too high (H),too low (L) or correct(C)? ")
        if feedback == 'h':    # h for high
            high = comp_guess - 1
        elif feedback == 'l':    # l for low
            low = comp_guess + 1

    print(f"Yay! The computer guessed your number {comp_guess} correctly!")


x = int(input("Enter the number of guessing range: "))

computer_guesses_range(x)
