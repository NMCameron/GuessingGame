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

while guessed == False:

    guess = input("Guess an odd number 1-1000: ").strip()
    if (guess.isdigit()):

        if (int(guess) == answer):
            print("\nCongrats! You guessed the number! (", answer, ")")
            print("Thanks for playing!")
            guessed = True

        elif (int(guess) < answer):
            print("The number is greater than", guess, "\n")

        else:
            print("The number is less than", guess,"\n")
            
    else:
          print("Please enter a number\n")
    