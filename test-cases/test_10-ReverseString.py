import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

module = __import__('10-ReverseString') # Import the python file for testing 

# Test cases with pytest
def test_case1():
    
    
    assert module.reverse("Ryan") == "nayR", "the name ryan should return as nayR"

def test_case2():

    assert module.reverse("Yo Yo Yo , its me a Mario") == "oiraM a em sti , oY oY oY" ,"the phrase should be reversed" 
