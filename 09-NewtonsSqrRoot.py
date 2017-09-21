'''
Newtons Square Root
Author: Ryan Gordon
Date: 21/09/17
Implement the square root function using Newton's method.
In this case, Newton's method is to approximate sqrt(x) by picking a starting point z and then repeating:
'''
import math
from decimal import *
# Initialise variables
iterations = 0
difference = 1

# Get a number to square root and also a guess to start from 
try:
    x = Decimal(input("Enter a number: "))
    z = Decimal(input("Starting point (Best guess): "))

    # Approximate using newtons method
    approximate = z - ((z*z - x) / (2 * z))
    print("Approximating.... \n")
    # Loop until we have approximated close enough to the real squareroot
    while difference > 0.0000000001:
        print(z,approximate)
        z = approximate
        approximate = z - ((z*z - x) / (2 * z))
        difference = z - approximate
        iterations = iterations + 1

    # Accurate sqrt using Math library
    
    print("\nMath.sqrt(x) method: \t" + str(round( Decimal( math.sqrt(x) ),4))) 
    # Newtons method
    print("Newton's Method: \t" + str(round(Decimal(approximate),4)))
    # Iterations needed to approximate the root
    print("Iterations needed : \t"+str(iterations))
#Catch when a non number or empty input is entered        
except InvalidOperation:
    print('Non-numeric data found in the input. Try again')