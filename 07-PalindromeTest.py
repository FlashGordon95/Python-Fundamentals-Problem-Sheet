"""
Plaindrome Test
Author: Ryan Gordon
Date: 21/09/17

Write a function that tests whether a string is a palindrome.
Ryan Gordon -

"""

comparisonString = ""

def reverse(text):
    if len(text) <= 1:
        return text
    # Take the first char and paste it onto the end of the string
    return reverse(text[1:]) + text[0]

def palindromeTest(testString):
    comparisonString = reverse(testString)

    if comparisonString.lower() == testString.lower():
        print(testString+" is a palindrome")
        return True;
    else:
        print(testString+" is not palindrome")
        return False;
palindromeTest("Assa")
palindromeTest("Ryan")

"""
Assa is a palindrome
Ryan is not palindrome
"""