'''
Factorial digit sum
Author: Ryan Gordon
Date: 21/09/17

n! means n*(n-1)x....
For example, 10! = 10x9x8x7x6x5x4x3x2x1 = 3628800
sum the digits in the number 10! is 3+6+2+8+8+0+0 = 27
Find the sum of the digits in the number 100!
Adapted from my other repo: https://github.com/FlashGordon95/Project-Euler-Solutions/blob/master/FactorialDigitSum-Problem20.py
Ryan Gordon -
'''
# Standard factorial function
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1) # Recursively call fact until we have gone through all facts


def factDigitSum(n):
    
    return sum([int(i) for i in str(fact(n))])
factNum = fact(100) # Calls the fact function, number given is the factorial
# from one of my other solutions. Split the int into singular digits in a list
# we then call sum on this list
print(factDigitSum(100))

'''
Input
100 
Output 
648
'''