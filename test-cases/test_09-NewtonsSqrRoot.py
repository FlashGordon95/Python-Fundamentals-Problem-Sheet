import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

module = __import__('09-NewtonsSqrRoot') # Import the python file for testing 

# Test cases with pytest
def test_case1():
    assert module.newtons_root(16, 1) == (4.0,6), "newtons root to get root of 16 should be 4 with 6 iterations starting from 1"

def test_case2():
    assert module.newtons_root(144, 12) == (12.0,1), "newtons root to get root of 144 should be 12 with 1 iterations starting from 12"