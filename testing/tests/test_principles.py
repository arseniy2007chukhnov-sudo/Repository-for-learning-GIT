import sys
# TODO make with 'pip install -e .
sys.path.append("../src")

from math_demo import (add, add_with_bug, add_something)

def test_addition_basic():
    assert add(2,2) == 4, "Function didn't returned 4" 
    print("Test BASIC ADDITION PASSED")

def test_bug_addition_notsufficient():
    assert add_with_bug(2,2) == 4, "Function didn't returned 4" 
    print("Test BUG ADDITION PASSED")


def test_bug_addition_enough():
    assert add_with_bug(2, 2) == 4, "Function didn't returned"
    assert add_with_bug(0, 0) == 0
    #assert add_with_bug(5, 6) == 11 # WILL fail if uncommented
    print("Test BUG ADDITION PASSED")

def test_addition_duplicated_logic():
    # VERY BAD TEST -
    assert add(6, 3) == 6 + 3
    print ("Test DUPLICATED LOGIC PASSED (could get some bugs in the future)")
    # VERY GOOD TEST +
    assert add(6, 3) == 9
    print ("Test DUPLICATED LOGIC PASSED")

def test_addition_overcomplicated():
    # would work but slow and not actually needed
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i, j) == i + j # bad since violates "duplication"
            assert add(-i, j) == -i + j
            assert add(i, -j) == i - j
            assert add(-i, -j) == -i - j

def test_addition_reasonable():
    assert add(6, 3) == 9
    assert add(0, 3) == 3
    assert add(0, -3) == -3
    assert add(-7, 83) == 76
    assert add(-7, -83) == -90
    print("Test ADDITION with REASONABLE NUMBER of CASES PASSED")

def test_add_something_reasonable():
    assert add(6, 3) == 9
    assert add(0, 3) == 3
    assert add(0, -3) == -3
    assert add(-7, 83) == 76
    assert add(-7, -83) == -90
    add_something(None, None) == 0
    add_something(None, "abc")== 0
    add_something(None, 10) == 0
    add_something("abc", 10) == "abc10"
    add_something(10, 'abc') == "10abc" 
    add_something("xyz", "abc") == "xyzabc"
    print("Test ANOTHER ADDITION with REASONABLE NUMBER of CASES PASSED")


if __name__ == "__main__":
    test_addition_basic()
    test_bug_addition_notsufficient()
    test_addition_duplicated_logic()
    test_bug_addition_enough()
    test_addition_reasonable()
    test_add_something_reasonable()