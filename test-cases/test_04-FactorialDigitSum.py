import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

fact = __import__('04-FactorialDigitSum') # Import the python file for testing 

# Test cases with pytest
def test_case1():
    assert fact.factDigitSum(100)== 648, "the fact digit sum of 100 should be 648"
def test_case2():
    assert fact.factDigitSum(10) == 27, "the fact digit sum of 100 should be 648"

def test_case3():
    assert fact.fact(10) == 3628800, "the fact of 10 should be 3628800"