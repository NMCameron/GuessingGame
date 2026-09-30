"""
Each group will create a GitHub repository focused on developing a guessing game that allows players to guess an odd integer between 1 and 1000.
"""
import random as rand

number = rand.randint(0,999)
if number % 2 == 0:
    answer = number + 1
else:
    answer = number

guessed = False
while int(guessed) == False:
    guess = input("Guess an odd number 1-1000: ")
    if int(guess) == answer:
        print("Congrats! You guessed ")
        guessed = True
    elif int(guess) < answer:
        print(guess, "is less than the number")
    else:
        print(guess, "is bigger than the number")