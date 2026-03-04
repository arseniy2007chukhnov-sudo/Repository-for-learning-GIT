import sys
# TODO make with 'pip install -e .
sys.path.append("../src")

from math_demo import (add, add_with_bug)

def test_addition_basic():
    assert add(2,2) == 4, "Function didn't returned 4" 
    print("Test BASIC ADDITION PASSED")

def test_bug_addition_notsufficient():
    assert add_with_bug(2,2) == 4, "Function didn't returned 4" 
    print("Test BUG ADDITION PASSED")


def test_bug_addition_enough():
    assert add_with_bug(2, 2) == 4, "Function didn't returned"
    assert add_with_bug(0, 0) == 0
    assert add_with_bug(5, 6) == 11
    print("Test BUG ADDITION PASSED")

def test_addition_duplicated_logic():
    # VERY BAD TEST -
    assert add(6, 3) == 6 + 3
    # VERY GOOD TEST +
    assert add(6, 3) == 9
    print ("Test DUPLICATED LOGIC PASSED")

if __name__ == "__main__":
    test_addition_basic()
    test_bug_addition_notsufficient()
    test_addition_duplicated_logic()
    test_bug_addition_enough()