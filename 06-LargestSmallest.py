"""
Largest smallest in a list
Author: Ryan Gordon
Date: 21/09/17

Write a function that returns the largest and smallest elements in a list.

Enhancement: Generate a random list of integers and return the largest and smallest elements 
Ryan Gordon -

"""
import random

testList = [1,2,3,4,5]
testList2 = [int(10*random.random()) for i in range(10)]
def largeSmall(list):

    return min(list), max(list)


print(largeSmall(testList))
print(testList2)
print(largeSmall(testList2))

"""
Output (example):

(1, 5)
[5, 7, 6, 7, 2, 2, 2, 4, 3, 4]
(2, 7)
"""