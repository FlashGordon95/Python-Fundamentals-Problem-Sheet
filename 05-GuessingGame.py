"""
Guessing game
Author: Ryan Gordon
Date: 21/09/17

Write a guessing game where the user must guess a secret number. 
After every guess the program tells the user whether their number was too large or too small. 
At the end the number of tries needed should be printed. 
It counts only as one try if they input the same number multiple times consecutively.
Ryan Gordon -

Resources:
Python exceptions: http://www.pythonforbeginners.com/error-handling/exception-handling-in-python
"""

import random

guessedCorrect = False
tries = 0
previousGuesses = set()
targetNumber = random.randint(0, 20)

while (guessedCorrect is False):
    try:
        var = int(input("Previous tries "+str(tries)+"\n Please enter a number to guess: "))
        print ("you entered", var)

        # Check if they guessed correctly
        if (targetNumber == var):
        print("You guessed correct! Number is "+ str(targetNumber))
        guessedCorrect=True

        else:
            #If they enter the same incorrect guess dont add to attempts
            if(var not in previousGuesses):
                previousGuesses.add(var)
                tries = tries + 1
        
            #number is too small
            if(var<targetNumber):
                print("Guess is too small")
            #number is too large    
            elif(var>targetNumber):
                print("Guess is too large")
        #Catch when a non number or empty input is entered        
        except ValueError:
            print('Non-numeric data found in the file. Try again')
    
            