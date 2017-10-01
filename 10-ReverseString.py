'''
Reverse String
Author: Ryan Gordon
Date: 21/09/17
Write a function to reverse a string.

'''


def reverse(text):
    if len(text) <= 1:
        return text
    # Take the first char and paste it onto the end of the string
    return reverse(text[1:]) + text[0]
# Test String
string = "Yo Yo Yo , its me a Mario"
print(string)
print(reverse(string))

'''
Output
Yo Yo Yo , its me a Mario
oiraM a em sti , oY oY oY
'''