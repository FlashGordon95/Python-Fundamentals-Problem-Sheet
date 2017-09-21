'''
FizzBuzz
Author: Ryan Gordon
Date: 21/09/17
Write a program that prints the numbers from 1 to 100, except for the following conditions.
For multiples of three print "Fizz" instead of the number, and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

'''


for x in range(100):
    if x % 3 == 0 and x % 5 == 0:
     print('FizzBuzz');
    elif x % 3 == 0:
        print('Fizz');
    elif x % 5 == 0:
        print('Buzz');
    else:
        print(str(x))
