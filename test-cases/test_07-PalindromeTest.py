import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

module = __import__('07-PalindromeTest') # Import the python file for testing 

# Test cases with pytest
def test_case1():
    test_word = "Banana"

    assert module.palindromeTest(test_word) is False, "the largest and smallest of the list should be returned"

def test_case2():
    test_word = "Assa"

    assert module.palindromeTest(test_word) is True