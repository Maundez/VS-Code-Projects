import pytest
from um import count

def test_count_correct_behavior():
    # Test for correct behavior
    assert count("hello, um, world") == 1
    assert count("yummy food") == 0
    assert count("um in the beginning") == 1
    assert count("ends with um") == 1
    assert count("Um with capital") == 1
    assert count("multiple um um occurrences") == 2

def test_count_incorrect_behavior_substring():
    # Test for incorrect behavior: counting "um" in a substring
    assert count("yummy food") == 0
    assert count("plum and mums") == 0

def test_count_incorrect_behavior_space_requirement():
    # Test for incorrect behavior: requiring spaces around "um"
    assert count("um, comma before") == 1
    assert count("after um.") == 1
    assert count("um!") == 1
