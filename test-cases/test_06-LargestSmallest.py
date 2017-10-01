import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

module = __import__('06-LargestSmallest') # Import the python file for testing 

# Test cases with pytest
def test_case1():
    testlist = [9,5,3,44,77]
    assert module.largeSmall(testlist)== (3,77), "the largest and smallest of the list should be returned"
