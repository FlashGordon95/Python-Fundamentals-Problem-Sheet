"""
Largest smallest in a list
Author: Ryan Gordon
Date: 21/09/17

Write a function that returns the largest and smallest elements in a list.
Ryan Gordon -

"""


testList = [1,2,3,4,5]
def largeSmall(list):

    return min(list), max(list)


print(largeSmall(testList))