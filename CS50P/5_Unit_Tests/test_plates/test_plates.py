import pytest
from plates import is_valid

def test_is_valid_chars_count():
    assert is_valid("H") == False
    assert is_valid("HELL") == True
    assert is_valid("HEL123") == True
    assert is_valid("HELLOSTS") == False
    
def test_is_valid_alpha_count():
    assert is_valid("A123") == False
    assert is_valid("AA123") == True

def test_is_valid_numbers():
    assert is_valid("ABC012") == False  # Checks 0 is not the first digit
    assert is_valid("ABC123") == True
    assert is_valid("ABC12D") == False
    assert is_valid("12345") == False  
    assert is_valid("123ABC") == False
    
def test_is_valid_punctuation():
    assert is_valid("ABC 01") == False 
    assert is_valid("ABC-12") == False
    assert is_valid("!BC12") == False
    assert is_valid("AB.125") == False  
    assert is_valid(".ABC12") == False
    
    
