
'''
Merge List and Sort
Author: Ryan Gordon
Date: 21/09/17
Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6].

'''

# Specify two lists
listone = [99,1 ,4 ,6,8,24]
listtwo = [2 ,3 ,5]

# Create third list from the first 2
listthree = listone + listtwo
print("Before sort :" )
print(listthree)
listthree.sort()



print ("After sort : ")
print (listthree)

'''
Output
Before sort :
[99, 1, 4, 6, 8, 24, 2, 3, 5]
After sort :
[1, 2, 3, 4, 5, 6, 8, 24, 99]
'''