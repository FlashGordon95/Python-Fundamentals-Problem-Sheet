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



def newtons_root(x,z):
    difference = 1
    iterations = 0
    # Newtons root formulae
    approximate = z - ((z*z - x) / (2 * z))
    print("Approximating.... \n")
    # Loop until we have approximated close enough to the real squareroot
    while difference > 0.0000000001:
        print(z,approximate)
        z = approximate
        approximate = z - ((z*z - x) / (2 * z))
        difference = z - approximate
        iterations = iterations + 1

    return approximate, iterations
# Get a number to square root and also a guess to start from 
try:
    x = Decimal(input("Enter a number: "))
    z = Decimal(input("Starting point (Best guess): "))

    # Approximate using newtons method
    approximate,iterations = newtons_root(x,z)

    # Accurate sqrt using Math library
    print("\nMath.sqrt(x) method: \t" + str(round( Decimal( math.sqrt(x) ),4))) 
    # Newtons method
    print("Newton's Method: \t" + str(round(Decimal(approximate),4)))
    # Iterations needed to approximate the root
    print("Iterations needed : \t"+str(iterations))
#Catch when a non number or empty input is entered        
except InvalidOperation:
    print('Non-numeric data found in the input. Try again')
except:
    print('Exception raised but not by the input')

'''
Input / Output
Enter a number: 16
Starting point (Best guess): 1
Approximating....

1 8.5
8.5 5.191176470588235294117647059
5.191176470588235294117647059 4.136664722546242292951174804
4.136664722546242292951174804 4.002257524798522343899464377
4.002257524798522343899464377 4.000000636692939467945433961
4.000000636692939467945433961 4.000000000000050672229330379

Math.sqrt(x) method:    4.0000
Newton's Method:        4.0000
Iterations needed :     6
'''
